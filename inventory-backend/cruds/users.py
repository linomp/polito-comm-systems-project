from core import db_functions
from schemas.user import User


async def add_user(new_user: User):
    values = {"user_id": new_user.user_id, 
              "name": new_user.name, 
              "mail_adr": new_user.mail_adr, 
              "hashed_pw": new_user.hashed_pw, 
              "salt": new_user.salt,
              "rfid": new_user.user_id, 
              "pin": new_user.pin
              }

    query = "INSERT INTO users(user_id, name, mail_adr, hashed_pw, salt, rfid, pin) VALUES (:user_id, :name, :mail_adr, :hashed_pw, :salt, :rfid, :pin)"
    await db_functions.execute(query=query, values=values)

    return 


async def update_users_card(user: User): #NAO SEI SE FUNCIONA
    values = {"rfid": user.rfid, 
              "pin": user.pin
              }
    query = "UPDATE users SET rfid=:rfid, pin=:pin WHERE user_id={user.user_id}"
    await db_functions.execute(query=query, values=values)

    return


async def get_user_from_id(user_id: int):
    query = f"SELECT id, user_id, name, mail_adr, hashed_pw, salt, rfid, pin FROM users WHERE user_id={user_id}"
    data = await db_functions.fetch_one(query)

    return data


async def get_user_from_email(mail_adr: str):
    query = f"SELECT id, user_id, name, mail_adr, hashed_pw, salt, rfid, pin FROM users WHERE mail_adr={mail_adr}"
    data = await db_functions.fetch_one(query)

    return data


async def get_user_from_rfid(rfid: int):
    query = f"SELECT id, user_id, name, mail_adr, hashed_pw, salt, rfid, pin FROM users WHERE rfid={rfid}"
    data = await db_functions.fetch_one(query)

    return data
