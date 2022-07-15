from dependencies import db
from schemas.user import User
from services.auth import get_password_hash


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


def update_users_card(user: User):
    values = (user.rfid,
              user.pin,
              user.id
              )
    query = "UPDATE users SET rfid=%s, pin=%s WHERE id=%s"
    db.execute(query, values)

    return


def get_user_from_id(user_id: int):
    values = (user_id,)
    query = "SELECT * FROM users WHERE id=%s"
    data = db.fetch_one(query, values)

    if data is None:
        return None

    new_user = User(id=data[0], name=data[1], mail_adr=data[2],
                    hashed_pw=data[3], salt=data[4], rfid=data[5], pin=data[6])

    return new_user


def get_user_from_email(mail_adr: str):
    values = (mail_adr,)
    query = "SELECT id, name, mail_adr, hashed_pw, salt, rfid, pin FROM users WHERE mail_adr=%s"
    data = db.fetch_one(query, values)

    if data is None:
        return None

    new_user = User(id=data[0], name=data[1], mail_adr=data[2],
                    hashed_pw=data[3], salt=data[4], rfid=data[5], pin=data[6])

    return new_user


def get_user_from_rfid(rfid: str):
    values = (rfid,)
    query = "SELECT id, name, mail_adr, hashed_pw, salt, rfid, pin FROM users WHERE rfid=%s"
    data = db.fetch_one(query, values)

    if data is None:
        return None

    new_user = User(id=data[0], name=data[1], mail_adr=data[2],
                    hashed_pw=data[3], salt=data[4], rfid=data[5], pin=data[6])

    return new_user


def remove_user(user_id: int):
    values = (user_id,)
    query = "DELETE FROM users WHERE id=%s"
    db.execute(query, values)

    return


def get_role_costumer(user_id: int, costumer_id: int):
    values = (user_id,
              costumer_id)
    query = "SELECT role FROM users2costumers WHERE user_id=%s AND cst_id=%s"
    data = db.fetch_one(query, values)

    if data is None:
        return None
    else:
        return data[0]


def get_all_csts_from_user(user_id: int):
    values = (user_id,)
    query = "SELECT * FROM users2costumers WHERE user_id=%s"
    data = db.fetch_all(query, values)

    return data
