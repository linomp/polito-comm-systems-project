import mysql.connector as con
from mysql.connector import Error


def create_connection(host_name, user_name, user_password):
    global connection
    connection =None
    try:
        connection = con.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
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
    

async def execute(query, data): #EXECUTE SEM CONN??
    cursor = connection.cursor()
    try:
        cursor.execute(query, data)
        connection.commit()
        print("Query executed")
    except Error as e:
        print(f"The error '{e}' occurred")
        connection.rollback()
    cursor.close()

    return


async def fetch_all(query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        all=cursor.fetchall()
    except Error as e:
        print(f"The error '{e}' occurred")
    cursor.close()
    return


async def fetch_one(query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        all=cursor.fetchone()
    except Error as e:
        print(f"The error '{e}' occurred")
    cursor.close()
    return







