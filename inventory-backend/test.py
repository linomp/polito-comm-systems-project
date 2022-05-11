from asyncio.windows_events import NULL
import mysql.connector as con
from mysql.connector import Error
from core import db_functions
from cruds import costumers, items, users
from schemas import costumer, item, user


try:
    db_functions.create_connection("localhost", "root", "sqlpassword")
    
    
    new_user = user.User(id=None, user_id=4, name="Marcus Fiorentino", mail_adr="marcusfiorentino@gmail.com",  
                            hashed_pw=None, salt=None, rfid=None, pin=None)
    password ="password"
    users.add_user(new_user, password)
    

    '''    
    user_test = user.User(id=3, user_id=2, name="", mail_adr="", 
                            hashed_pw="", salt="", rfid=30, pin=1234)    
    users.update_users_card(user_test)
    '''

    '''
    id=4
    password ="password "

    if (users.check_password(id, password)):
        print("DEU CERTO")
    else:
        print("DEU ERRADO")
    '''

    '''
    id=1
    password ="password"
    users.change_password(id, password)
    '''
    

    db_functions.close_connection()

except Error as e:
    print(f"The error '{e}' occurred")



    