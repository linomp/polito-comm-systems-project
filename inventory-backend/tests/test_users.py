import uuid

from fastapi.testclient import TestClient

from components.constants import *

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

        response = client.post("/token", data=b"username=john@test.com&password=password",
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
            "name": test_name,
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


def test_update_card():
    with TestClient(app) as client:
        # Create new user
        test_mail = uuid.uuid4().hex + "@example.com"
        test_password = "password"
        response = client.post("/users", json={
            "mail_adr": test_mail,
            "name": "CONTROLLER TEST USER",
            "password": "password"
        })
        assert response.status_code == 200

        # Login with that user
        response = client.post("/token", data=f"username={test_mail}&password={test_password}".encode('utf-8'),
                               headers={
                                   'Content-Type': 'application/x-www-form-urlencoded'
                               })
        assert response.status_code == 200

        resp_body = response.json()
        assert "access_token" in resp_body
        assert "token_type" in resp_body

        # Perform card update operation
        expected_response = {
            "rfid": uuid.uuid4().hex,
            "pin": 1234
        }

        response_card = client.post("/users/card/update_card",
                                    headers={'Authorization': f'{resp_body["token_type"]} {resp_body["access_token"]}'},
                                    json={
                                        "rfid": expected_response["rfid"],
                                        "pin": expected_response["pin"]
                                    })
        assert response_card.status_code == 200

        resp_card = response_card.json()

        assert resp_card["rfid"] == expected_response["rfid"]
        assert resp_card["pin"] == expected_response["pin"]



def test_login_card():
    with TestClient(app) as client:
        # Create new user
        test_mail = uuid.uuid4().hex + "@example.com"
        test_password = "password"
        response = client.post("/users", json={
            "mail_adr": test_mail,
            "name": "CONTROLLER TEST USER",
            "password": "password"
        })
        assert response.status_code == 200

        # Login with that user
        response = client.post("/token", data=f"username={test_mail}&password={test_password}".encode('utf-8'),
                               headers={
                                   'Content-Type': 'application/x-www-form-urlencoded'
                               })
        assert response.status_code == 200

        resp_body = response.json()
        assert "access_token" in resp_body
        assert "token_type" in resp_body

        # Perform card update operation
        expected_response = {
            "rfid": uuid.uuid4().hex,
            "pin": 1234
        }

        response_card = client.post("/users/card/update_card",
                                    headers={'Authorization': f'{resp_body["token_type"]} {resp_body["access_token"]}'},
                                    json={
                                        "rfid": expected_response["rfid"],
                                        "pin": expected_response["pin"]
                                    })
        assert response_card.status_code == 200

        resp_card = response_card.json()

        assert resp_card["rfid"] == expected_response["rfid"]
        assert resp_card["pin"] == expected_response["pin"]

        #login with card
        response_login = client.post("/users/card/login",
                                    json={"rfid": resp_card["rfid"],
                                        "pin": resp_card["pin"]})
        assert response.status_code == 200

        resp_login = response_login.json()

        assert resp_login["mail_adr"] == test_mail
    


def test_add_client_to_cst():
    with TestClient(app) as client:
        # Create new customer
        test_name = uuid.uuid4().hex
        test_category = "CUSTOMER CATEGORY TEST"

        response = client.post("/customers/new_cst", json={
            "name": test_name,
            "category": test_category
        })
        assert response.status_code == 200
        resp_costumer = response.json()

        # Create new user
        test_mail = uuid.uuid4().hex + "@example.com"
        response = client.post("/users", json={
            "mail_adr": test_mail,
            "name": "CONTROLLER TEST USER",
            "password": "password"
        })
        assert response.status_code == 200
        resp_user = response.json()

        test_cst_mail=test_name + DEFAULT_ADMIN_USER_SUFFIX

        # Log in with admin
        response = client.post("/token", data=f"username={test_cst_mail}&password={DEFAULT_USER_PASSWORD}".encode('utf-8'),
                               headers={
                                   'Content-Type': 'application/x-www-form-urlencoded'
                               })
        assert response.status_code == 200

        resp_login = response.json()
        assert "access_token" in resp_login
        assert "token_type" in resp_login
        

        #test adding client
        response = client.post(f"/users/employees/add_client?new_client_id={resp_user['id']}&costumer_id={resp_costumer['id']}",
                                    headers={'Authorization': f'{resp_login["token_type"]} {resp_login["access_token"]}'})
        assert response.status_code == 200
