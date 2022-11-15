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
    assert response.headers['Location'] == '/login'


def test_login(client, auth):
    assert client.get('/login').status_code == 200
    response = auth.login()
    #assert response.headers["Location"] == "/login"

    with client:
        client.get('/')
        assert session['user_id'] == 1
        assert session['username'] == 'admin'


def test_logout_functionality(client, auth):
    auth.login()

    with client:
        auth.logout()
        assert 'user_id' not in session


def test_register(client, app):
    assert client.get('/register').status_code == 200
    response = client.post(
        '/register', data={'username': 'abcd', 'password1': '123456', 'password2': '123456'})
