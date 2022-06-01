import sys

import mysql.connector as con
from mysql.connector import Error

from env import *


class DBComponent:
    def __init__(self, host_name=DB_HOST, user_name=DB_USER, user_password=DB_PASSWORD, database=DB_NAME, port=DB_PORT):
        self.connection = None
        self.host_name = host_name
        self.user_name = user_name
        self.user_password = user_password
        self.database = database
        self.port = port

    def create_connection(self):
        try:
            self.connection = con.connect(
                host=self.host_name,
                user=self.user_name,
                passwd=self.user_password,
                database=self.database,
                port=self.port
            )
            print("Connection to MySQL DB successful")
        except Error as e:
            print(f"The error '{e}' occurred trying to connect to MySQL DB {self.database}")
            sys.exit(1)

    def close_connection(self):
        try:
            self.connection.close()
            print("Closing MySQL DB successful")
        except Error as e:
            print(f"The error '{e}' occurred")
        return

    # TODO: refactor to actually return the error upstream.
    #       If something goes wrong, it gets lost here and then we have no fucking idea
    def execute(self, query, data):
        cursor = self.connection.cursor()

        try:
            cursor.execute(query, data)
            self.connection.commit()
            print("Query executed")
        except Error as e:
            self.connection.rollback()
            raise Exception(e)
        cursor.close()

        return

    def fetch_all(self, query, data):
        cursor = self.connection.cursor()
        result = None

        try:
            cursor.execute(query, data)
            result = cursor.fetchall()
        except Error as e:
            print(f"The error '{e}' occurred")
        cursor.close()

        return result

    def fetch_one(self, query, data):
        cursor = self.connection.cursor()
        result = None

        try:
            cursor.execute(query, data)
            result = cursor.fetchone()
        except Error as e:
            print(f"The error '{e}' occurred")
        cursor.close()

        return result
