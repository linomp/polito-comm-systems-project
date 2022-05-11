from asyncio.windows_events import NULL

from sympy import satisfiable
from core import db_functions
from schemas.user import User
import bcrypt


def add_user(new_user: User, password: str):

    hashed, salt = hash_password(password)
    
    

    values = (NULL,
            new_user.user_id, 
            new_user.name, 
            new_user.mail_adr,
            hashed,
            salt,
            new_user.rfid, 
            new_user.pin
            )

    query = ("INSERT INTO users (id, user_id, name, mail_adr, hashed_pw, salt, rfid, pin) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
    db_functions.execute(query, values)
    

    return 


def change_password(user_id: int, pwd: str):

    hashed, salt = hash_password(pwd)

    values = ( hashed,
               salt,
               user_id 
              )
    
    query = "UPDATE users SET hashed_pw=%s, salt=%s WHERE user_id=%s"
    db_functions.execute(query, values)
    
    return


def check_password(user_id: int, pwd: str):

    user = get_user_from_id(user_id)

    return bcrypt.checkpw(pwd.encode('utf-8'), user.hashed_pw.encode('utf-8'))


def hash_password(password: str):

    bytePwd = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(bytePwd, salt)
    
    return hashed, salt



def update_users_card(user: User): #NAO SEI SE FUNCIONA
    
    values = (user.rfid, 
              user.pin,
              user.user_id
            )
    query = "UPDATE users SET rfid=%s, pin=%s WHERE user_id=%s"
    db_functions.execute(query, values)

    return


def get_user_from_id(user_id: int):
    values = (user_id,)
    query = "SELECT id, user_id, name, mail_adr, hashed_pw, salt, rfid, pin FROM users WHERE user_id=%s"
    data = db_functions.fetch_one(query, values)

    new_user = User(id=data[0], user_id=data[1], name=data[2], mail_adr=data[3], 
                    hashed_pw=data[4], salt=data[5], rfid=data[6], pin=data[7])

    return new_user


def get_user_from_email(mail_adr: str):
    values = (mail_adr,)
    query = "SELECT id, user_id, name, mail_adr, hashed_pw, salt, rfid, pin FROM users WHERE mail_adr=%s"
    data = db_functions.fetch_one(query, values)

    new_user = User(id=data[0], user_id=data[1], name=data[2], mail_adr=data[3], 
                    hashed_pw=data[4], salt=data[5], rfid=data[6], pin=data[7])

    return new_user


def get_user_from_rfid(rfid: int):
    values = (rfid,)
    query = "SELECT id, user_id, name, mail_adr, hashed_pw, salt, rfid, pin FROM users WHERE rfid=%s"
    data = db_functions.fetch_one(query, values)

    new_user = User(id=data[0], user_id=data[1], name=data[2], mail_adr=data[3], 
                    hashed_pw=data[4], salt=data[5], rfid=data[6], pin=data[7])

    return new_user


def remove_user(user_id: int):

    values = (user_id,)
    query = "DELETE FROM users WHERE user_id=%s"
    db_functions.execute(query, values)

    return

