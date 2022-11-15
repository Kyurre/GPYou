import sqlite3
import pytest

@pytest.fixture()
def session():
    connection = sqlite3.connect((':memory'))
    db_session = connection.cursor()
    yield db_session
    connection.close()

@pytest.fixture()
def setup_db(session):
    session.execute('''
        CREATE TABLE IF NOT EXISTS USERS (
                    user_id     SERIAL UNIQUE PRIMARY KEY,
                    username    TEXT NOT NULL UNIQUE,
                    password    TEXT NOT NULL,
                    isAdmin     BOOL DEFAULT FALSE
    ''')