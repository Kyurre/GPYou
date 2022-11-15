from flask import Flask
from website.db_conn import get_db_conn
from website.db_tables import create_tables
from website.db_insert import insert_to_db, create_admin
import psycopg2
# website.NeweggScraper as NWS
#import website.amazonscrapper as AWSC


def create_app():
    app = Flask(__name__)
    app.secret_key = "supersecret!"

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    # glist = NWS.NewEggScrapperFunc() # ls 11/09/2022 using Kosta's scraper to init database GPU table
    # AWSC.runSearch("gpu")  # ls 11/09/2022 using Dave's scraper to init the DB
    create_tables()  # current drops all table use other functions to drop specific ones later
    create_admin()

    # provide path to csv and comment out durning pytest
    # insert_to_db('tests/gpu.csv')

    return app
