from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

global access_token
global token_type


def test_hello_world():
    response = client.get("/")
    assert response.status_code == 200

    resp_body = response.json()
    assert "message" in resp_body
    assert resp_body["message"] == "Hello from FastAPI + MySQL app w/o ORM"


def test_login_for_access_token():
    global access_token
    global token_type

    response = client.post("/token", data=b"username=johndoe&password=johndoe",
                           headers={
                               'Content-Type': 'application/x-www-form-urlencoded'
                           })
    assert response.status_code == 200

    resp_body = response.json()
    assert "access_token" in resp_body
    assert "token_type" in resp_body

    access_token = resp_body["access_token"]
    token_type = resp_body["token_type"]


def test_read_users_me():
    global access_token
    global token_type

    response = client.get("/users/me", headers={
        'Authorization': f'{token_type} {access_token}'
    })
    assert response.status_code == 200

    resp_body = response.json()
    assert resp_body == {
        "username": "johndoe",
        "email": "johndoe@example.com",
        "full_name": "John Doe",
        "disabled": False
    }
