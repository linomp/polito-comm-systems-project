from asyncio.windows_events import NULL
import mysql.connector as con
from mysql.connector import Error
from core import db_functions
from cruds import costumers, items, users
from schemas import costumer, item, user

async def test():

    try:
        db_functions.create_connection("localhost", "root", "sqlpassword")
        new_user = user.User(id=NULL, user_id=1, name="John Doe", mail_adr="johndoe@gmail.com", 
                             hashed_pw=NULL, salt=NULL, rfid=NULL, pin=NULL)
        await users.add_user(new_user)
        db_functions.close_connection()
    except Error as e:
        print(f"The error '{e}' occurred")

    return

await test()


    