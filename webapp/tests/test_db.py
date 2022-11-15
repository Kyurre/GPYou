from unittest.mock import MagicMock
import sqlite3
import pytest


@pytest.fixture()
def session():
    connection = sqlite3.connect('tutorial.db')
    db_session = connection.cursor()
    yield db_session
    connection.close()


@pytest.fixture
def setup_db(session):  # 2
    session.execute('''DROP TABLE IF EXISTS numbers''')
    session.execute('''CREATE TABLE numbers
                          (number text, existing boolean)''')
    session.execute('INSERT INTO numbers VALUES ("+3155512345", 1)')
    session.connection.commit()


@pytest.fixture
def cache(session):  # 1
    return CacheService(session)


@pytest.mark.usefixtures("setup_db")
def test_get(cache):  # 2
    existing = cache.get_status('+3155512345')
    assert existing


class CacheService:
    def __init__(self, session):  # 1
        self.session = session  # 2

    def get_status(self, number):
        self.session.execute(
            'SELECT existing FROM numbers WHERE number=?', (number,))
        return self.session.fetchone()

    def save_status(self, number, existing):
        self.session.execute(
            'INSERT INTO numbers VALUES (?, ?)', (number, existing))
        self.session.connection.commit()
