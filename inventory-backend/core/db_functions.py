from asyncio.windows_events import NULL
import mysql.connector as con
from mysql.connector import Error


def create_connection(host_name, user_name, user_password):
    global connection
    connection = None
    try:
        connection = con.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database="plcs_db"
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return 


def close_connection():
    try:
        connection.close()
        print("Closing MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return
    

def execute(query, data): 
    cursor = connection.cursor()
    try:
        print(query, data)
        cursor.execute(query, data)
        connection.commit()
        print("Query executed")
    except Error as e:
        print(f"The error '{e}' occurred")
        connection.rollback()
    cursor.close()

    return


def fetch_all(query, data):
    cursor = connection.cursor()
    try:
        cursor.execute(query, data)
        all=cursor.fetchall()
    except Error as e:
        print(f"The error '{e}' occurred")
    cursor.close()
    
    return all


def fetch_one(query, data):
    cursor = connection.cursor()
    try:
        cursor.execute(query, data)
        all=cursor.fetchone()
    except Error as e:
        print(f"The error '{e}' occurred")
    cursor.close()

    return all







