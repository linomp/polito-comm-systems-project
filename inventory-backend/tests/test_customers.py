import uuid

from starlette.testclient import TestClient

from components import constants
from main import app


def test_create_customer():
    with TestClient(app) as client:
        test_name = uuid.uuid4().hex
        test_category = "CUSTOMER CATEGORY TEST"

        response = client.post("/customers", json={
            "name": test_name,
            "category": test_category
        })
        assert response.status_code == 200

        resp_body = response.json()

        expected_response = {
            "name": test_name,
            "category": test_category,
            "default_user": {
                "name": constants.DEFAULT_USER_NAME,
                "mail_adr": test_name + constants.DEFAULT_ADMIN_USER_SUFFIX,
                "password": constants.DEFAULT_USER_PASSWORD
            }
        }

        for field in expected_response:
            assert field in resp_body
            assert resp_body[field] == expected_response[field]
