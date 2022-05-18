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

        response = client.post("/token", data=b"username=john@test.com&password=johndoe",
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

        expected_response = {
            "name": "John Doe",
            "mail_adr": "john@test.com",
            "rfid": None,
            "pin": None
        }

        for field in expected_response:
            assert field in resp_body
            assert resp_body[field] == expected_response[field]


def test_create_user():
    with TestClient(app) as client:
        test_mail = uuid.uuid4().hex + "@example.com"
        test_name = "CONTROLLER TEST USER"

        response = client.post("/users", json={
            "mail_adr": test_mail,
            "name": "CONTROLLER TEST USER",
            "password": "password"
        })
        assert response.status_code == 200

        resp_body = response.json()

        expected_response = {
            "name": test_name,
            "mail_adr": test_mail,
            "rfid": None,
            "pin": None
        }

        for field in expected_response:
            assert field in resp_body
            assert resp_body[field] == expected_response[field]
