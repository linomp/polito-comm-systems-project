import os

USER_ROLE_ADMIN = "ADMIN"
USER_ROLE_OPERATOR = "OPERATOR"
USER_ROLE_CLIENT = "CLIENT"

if os.getenv("ENV") == "TEST":
    DEFAULT_USER_NAME = "TEST_USER"
    DEFAULT_CUSTOMER_CATEGORY = "TEST CATEGORY"
    DEFAULT_USER_PASSWORD = "TEST_PASSWORD"
    DEFAULT_ADMIN_USER_SUFFIX = "@TEST"
    DEFAULT_USER_ROLE = USER_ROLE_CLIENT
else:
    DEFAULT_USER_NAME = "DEFAULT_USER"
    DEFAULT_ADMIN_USER_SUFFIX = "@admin"
    DEFAULT_USER_PASSWORD = "admin"
