from pydantic.main import BaseModel
from typing import Optional, Any


class User(BaseModel):
    id: Optional[int]
    name: str
    mail_adr: str
    hashed_pw: Optional[str]
    salt: Optional[str]
    rfid: Optional[str]
    pin: Optional[int]


class UserDAO(BaseModel):
    id: int
    name: str
    mail_adr: str
    rfid: Optional[str]
    pin: Optional[int]

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "name": "John Doe",
                "mail_adr": "john@test.com",
                "password": "password",
                "rfid": "1sdfsad-23456-sdf789",
                "pin": 1234
            }
        }


class NewUserDAO(BaseModel):
    name: str
    mail_adr: str
    rfid: Optional[str]
    password: str

    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe",
                "mail_adr": "john@test.com",
                "password": "password"
            }
        }
