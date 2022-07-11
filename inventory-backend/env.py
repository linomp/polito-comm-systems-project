import os

APP_ENV = os.environ.get("APP_ENV", "development")

DB_USER = os.environ.get("MYSQL_USER", "root")
DB_PASSWORD = os.environ.get("MYSQL_PASSWORD", "09d25e094faa6ca")
DB_HOST = os.environ.get("MYSQL_HOST", "apps.xmp.systems")
DB_PORT = os.environ.get("MYSQL_PORT", "443")
DB_NAME = os.environ.get("MYSQL_DATABASE", "plcs_db")

# to get a string like this run:
# openssl rand -hex 32
# SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
SECRET_KEY = "dummy-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
