from pydantic.main import BaseModel
from typing import Optional


class User(BaseModel):
    id: Optional[int]
    name: str
    mail_adr: str
    hashed_pw: Optional[str]
    salt: Optional[str]
    rfid: Optional[int]
    pin: Optional[int]


class NewUserDAO(BaseModel):
    name: str
    mail_adr: str
    password: str
