import mysql.connector as con
from mysql.connector import Error


def create_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = con.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


def close_connection(connection):
    connection.close()
    return
    

async def execute(connection, query, data): #EXECUTE SEM CONN??
    cursor = connection.cursor()
    try:
        # Execute the SQL command
        cursor.execute(query, data)
       # Commit your changes in the database
        connection.commit()
    except:
        # Rollback in case there is any error
        connection.rollback()
    cursor.close()

    return


async def fetch_all(query):
    return


async def fetch_one(query):
    return







