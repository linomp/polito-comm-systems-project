import os

APP_ENV = os.environ.get("APP_ENV", "development")

DB_USER = os.environ.get("MYSQL_USER", "root")
DB_PASSWORD = os.environ.get("MYSQL_PASSWORD", "admin")
DB_HOST = os.environ.get("MYSQL_HOST", "localhost")
DB_PORT = os.environ.get("MYSQL_PORT", "3306")
DB_NAME = os.environ.get("MYSQL_DATABASE", "plcs_db")
