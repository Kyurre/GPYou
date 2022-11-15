import psycopg2


# create a dabase connection


def get_db_conn():
    DB_HOST = 'database-hw3.cgv4f9hrnu6e.us-east-2.rds.amazonaws.com'
    DB_NAME = 'flask_db'
    DB_USER = 'postgres'
    DB_PASS = 'bu36yc5g'
    DB_PORT = 5432

    #DB_HOST = 'localhost'
    #DB_NAME = 'postgres'
    #DB_USER = 'postgres'
    #DB_PASS = 'bu36yc5g'
    #DB_PORT = 5432
    conn = psycopg2.connect(host=DB_HOST, dbname=DB_NAME,
                            user=DB_USER, password=DB_PASS, port=DB_PORT)

    return conn
