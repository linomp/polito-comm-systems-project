from pydantic.main import BaseModel


class User(BaseModel):
    id: int
    user_id: int
    name: str
    mail_adr: str
    hashed_pw: str
    salt: str
    rfid: int
    pin: int