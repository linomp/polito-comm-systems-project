from core import db_functions
from schemas.user import User


async def add_user(new_user: User):
    values = {"id": new_user.id,    #É PRECISO METER ID TABELA?
              "user_id": new_user.user_id, 
              "name": new_user.name, 
              "mail_adr": new_user.mail_adr, 
              "hashed_pw": new_user.hashed_pw, 
              "salt": new_user.salt
              }
              #DEFENIR NULL RFID E PIN

    query = "INSERT INTO users(id, user_id, name, mail_adr, hashed_pw, salt) VALUES (:id, :user_id, :name, :mail_adr, :hashed_pw, :salt)"
    insert_id = await db_functions.execute(query=query, values=values)

    return 


async def add_card_to_user(user_id: int):

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
