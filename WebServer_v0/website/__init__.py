from flask import Flask
import psycopg2
from os import path
from flask_login import LoginManager

def create_app():
    app = Flask(__name__)
    app.secret_key = "supersecret!"

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    #ls - From JD __init__.py (v.10242022)
    #from .models import User

    conn = get_db_conn()

    init_database(conn.cursor())

    return app

# connect to the database
def get_db_conn():
    conn = psycopg2.connect('dbname=gpuapp_db user=postgres password=postgres')
    return conn

def init_database(cur):
    #-ls from KK (v.10112022)
    #ls- user table
    cur.execute("""
        DROP TABLE IF EXISTS USERS;    
        CREATE TABLE USERS (
            user_email          TEXT NOT NULL PRIMARY KEY,
            user_pwd            TEXT,
            first_name          TEXT,
            isAdmin             BOOL DEFAULT FALSE,
            UNIQUE(user_email)
        );""")

    #ls- GPUS
    cur.execute("""
        DROP TABLE IF EXISTS GPUS;    
        CREATE TABLE GPUS (
            gpu_id          SERIAL UNIQUE,
            store           TEXT,
            gpu             TEXT,
            mnfctr          TEXT,
            mem             SMALLINT,
            price           MONEY,
            isInStock       BOOL, 
            isOnSale        BOOL 
        );""")

     #ls- Fav
    cur.execute("""
        DROP TABLE IF EXISTS FAV;    
        CREATE TABLE FAV (
            id          INTEGER,
            useremail        TEXT,
            CONSTRAINT fk_gpu FOREIGN KEY (id) REFERENCES GPUS(gpu_id),
            CONSTRAINT fk_useremail FOREIGN KEY (useremail) REFERENCES USERS(user_email)
        );""")

     #ls- populate deafults USER admin
    cur.execute("""INSERT INTO USERS(user_email, user_pwd, first_name, isAdmin) VALUES('lshah@depaul.edu', '1234', 'Luv', TRUE);""")

    #ls insert defaults GPUS
    cur.execute("""INSERT INTO GPUS(store, gpu, mnfctr, mem, price, isInStock, isOnSale) VALUES('Micro Center', 'GTX 3050', 'Asus', 8, 429.99, false,false);""")
    cur.execute("""INSERT INTO GPUS(store, gpu, mnfctr, mem, price, isInStock, isOnSale) VALUES('Micro Center', 'GTX 3050', 'MSI', 8, 339.99, true,true);""")
    cur.execute("""INSERT INTO GPUS(store, gpu, mnfctr, mem, price, isInStock, isOnSale) VALUES('Micro Center', 'GTX 3050', 'EVGA', 8, 329.99, true,true);""")
    cur.execute("""INSERT INTO GPUS(store, gpu, mnfctr, mem, price, isInStock, isOnSale) VALUES('Micro Center', 'GTX 3060', 'Nvidia', 12, 379.99, true,false);""")
    cur.execute("""INSERT INTO GPUS(store, gpu, mnfctr, mem, price, isInStock, isOnSale) VALUES('Micro Center', 'GTX 3060', 'Nvidia', 12, 399.99, true,false);""")
    cur.execute("""INSERT INTO GPUS(store, gpu, mnfctr, mem, price, isInStock, isOnSale) VALUES('Best Buy', 'GTX 3080', 'Asus', 8, 429.99, false,false);""")
    cur.execute("""INSERT INTO GPUS(store, gpu, mnfctr, mem, price, isInStock, isOnSale) VALUES('Best Buy', 'GTX 3080ti', 'MSI', 8, 339.99, true,true);""")
    cur.execute("""INSERT INTO GPUS(store, gpu, mnfctr, mem, price, isInStock, isOnSale) VALUES('Best Buy', 'GTX 3070', 'EVGA', 8, 329.99, true,true);""")
    cur.execute("""INSERT INTO GPUS(store, gpu, mnfctr, mem, price, isInStock, isOnSale) VALUES('Best Buy', 'GTX 3070 Super', 'Nvidia', 12, 379.99, true,false);""")
    cur.execute("""INSERT INTO GPUS(store, gpu, mnfctr, mem, price, isInStock, isOnSale) VALUES('Best Buy', 'GTX 3060', 'EVGA', 12, 399.99, true,false);""")

    