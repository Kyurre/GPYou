import pytest
from website import create_app

@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

class AuthActions(object):
    def __init__(self, client):
        self._client = client

    def login(self, username='dave', password='123456'):
        return self._client.post(
            '/login', data={'username': username, 'password': password}
        )

    def logout(self):
        return self._client.get('/logout')

@pytest.fixture()
def auth(client):
    return AuthActions(client)
