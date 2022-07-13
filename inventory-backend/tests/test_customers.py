import os
import uuid

from starlette.testclient import TestClient

# important for setting the values of constants file to the test values,
# which we also use for cleaning up the database
os.environ["ENV"] = "TEST"
from components import constants

from main import app

from dependencies import db


# Source: https://stackoverflow.com/a/40558283
class TestCustomers:

    @classmethod
    def teardown_class(cls):
        with TestClient(app) as client:
            query = "DELETE FROM costumers WHERE category LIKE %s;"
            db.execute(query, ('%TEST%',))

    def test_create_customer(self):
        with TestClient(app) as client:
            test_name = uuid.uuid4().hex
            test_category = constants.DEFAULT_CUSTOMER_CATEGORY

            response = client.post("/customers/new_cst", json={
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
