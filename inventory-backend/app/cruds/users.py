import bcrypt

from app.dependencies import db
from app.schemas.user import User


def add_user(new_user: User, password: str):
    hashed, salt = get_password_hash(password)

    values = (new_user.id,
              new_user.name,
              new_user.mail_adr,
              hashed,
              salt,
              new_user.rfid,
              new_user.pin
              )

    query = "INSERT INTO users (id, name, mail_adr, hashed_pw, salt, rfid, pin) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    db.execute(query, values)

    return


def change_password(user_id: int, pwd: str):
    hashed, salt = get_password_hash(pwd)

    values = (hashed,
              salt,
              user_id
              )

    query = "UPDATE users SET hashed_pw=%s, salt=%s WHERE id=%s"
    db.execute(query, values)

    return


# TODO: move this to service/auth
def verify_password(user_id: int, pwd: str):
    user = get_user_from_id(user_id)

    return bcrypt.checkpw(pwd.encode('utf-8'), user.hashed_pw.encode('utf-8'))


# TODO: move this to service/auth
def get_password_hash(password: str):
    bytePwd = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(bytePwd, salt)

    return hashed, salt


def update_users_card(user: User):  # NAO SEI SE FUNCIONA

    values = (user.rfid,
              user.pin,
              user.id
              )
    query = "UPDATE users SET rfid=%s, pin=%s WHERE id=%s"
    db.execute(query, values)

    return


def get_user_from_id(user_id: int):
    values = (user_id,)
    query = "SELECT id, name, mail_adr, hashed_pw, salt, rfid, pin FROM users WHERE id=%s"
    data = db.fetch_one(query, values)

    new_user = User(id=data[0], name=data[1], mail_adr=data[2],
                    hashed_pw=data[3], salt=data[4], rfid=data[5], pin=data[6])

    return new_user


def get_user_from_email(mail_adr: str):
    values = (mail_adr,)
    query = "SELECT id, name, mail_adr, hashed_pw, salt, rfid, pin FROM users WHERE mail_adr=%s"
    data = db.fetch_one(query, values)

    new_user = User(id=data[0], name=data[1], mail_adr=data[2],
                    hashed_pw=data[3], salt=data[4], rfid=data[5], pin=data[6])

    return new_user


def get_user_from_rfid(rfid: int):
    values = (rfid,)
    query = "SELECT id, name, mail_adr, hashed_pw, salt, rfid, pin FROM users WHERE rfid=%s"
    data = db.fetch_one(query, values)

    new_user = User(id=data[0], name=data[1], mail_adr=data[2],
                    hashed_pw=data[3], salt=data[4], rfid=data[5], pin=data[6])

    return new_user


def remove_user(user_id: int):
    values = (user_id,)
    query = "DELETE FROM users WHERE id=%s"
    db.execute(query, values)

    return
