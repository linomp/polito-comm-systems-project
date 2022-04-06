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
    

def add_user(connection, name, mail_adr, password):

    query = ("INSERT INTO users "
             "(id, user_id, name, mail_adr, hashed_pw, salt)")


    return 

def execute(connection, query, data):
    cursor = connection.cursor()
    cursor.execute(query, data)
    cursor.close()

    return





