import pytest
from flask import session, g

EC2 = "http://127.0.0.1:5000"


def test_can_call__ec2_endpoint(client):
    response = client.get(EC2)
    assert response.status_code == 308


def test_login_endpoint(client, auth):
    assert client.get('/login').status_code == 200


def test_admin_endpoint(client, auth):
    assert client.get('/admin').status_code == 200


def test_logout_endpoint(client):
    response = client.get("/logout")
    # Check that there was one redirect response.
    assert len(response.history) == 0
    # Check that the second request was to the index page.
    assert response.request.path == "/logout"


def test_login(client, auth):
    assert client.get('/login').status_code == 200
    response = auth.login()
    assert response.headers["Location"] == "/"

    with client:
        client.get('/')
        assert session['user_id'] == 1
        assert session['username'] == 'dkulis'


def test_logout(client, auth):
    auth.login()

    with client:
        auth.logout()
        assert 'user_id' not in session


"""
@pytest.mark.parametrize(('username', 'password', 'message'), (
    ('a', 'test', b'Incorrect username.'),
    ('test', 'a', b'Incorrect password.'),
))
def test_login_validate_input(auth, username, password, message):
    response = auth.login(username, password)
    assert message in response.data
    
"""
