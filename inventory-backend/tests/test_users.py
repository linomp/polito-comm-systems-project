import uuid

from fastapi.testclient import TestClient

from main import app

global access_token
global token_type


def test_hello_world():
    with TestClient(app) as client:
        response = client.get("/")
        assert response.status_code == 200

        resp_body = response.json()
        assert "message" in resp_body
        assert resp_body["message"] == "Hello from FastAPI + MySQL app w/o ORM"


def test_login():
    with TestClient(app) as client:
        global access_token
        global token_type

        response = client.post("/users/auth", data=b"username=johndoe&password=johndoe",
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
    with TestClient(app) as client:
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


def test_create_user():
    with TestClient(app) as client:
        test_mail = uuid.uuid4().hex + "@example.com"

        response = client.post("/users", json={
            "mail_adr": test_mail,
            "name": "CONTROLLER TEST USER",
            "password": "johndoe"
        })
        assert response.status_code == 200

        resp_body = response.json()
        assert resp_body["mail_adr"] == test_mail
        assert resp_body["name"] == "CONTROLLER TEST USER"
