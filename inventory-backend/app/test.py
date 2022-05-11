from mysql.connector import Error

from app.dependencies import db
from cruds import users
from schemas import user

try:

    db.create_connection()

    new_user = user.User(id=None, name="Maria Margarida", mail_adr="mariamargarida@gmail.com",
                         hashed_pw=None, salt=None, rfid=None, pin=None)
    password = "password"
    users.add_user(new_user, password)

    db.close_connection()


except Error as e:
    print(f"The error '{e}' occurred")
