from flask import sessions

EC2 = "http://127.0.0.1:5000/"

def test_can_call__ec2_endpoint(client):
    response = client.get(EC2)
    assert response.status_code == 200




def test_access_session(client):
    with client:
        response = client.post("http://127.0.0.1:5000/login", data={"username": "dae", "password": "123456"})
        print(response.status_code)

