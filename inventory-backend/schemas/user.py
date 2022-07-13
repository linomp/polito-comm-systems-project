from pydantic.main import BaseModel
from typing import Optional


class User(BaseModel):
    id: Optional[int]
    name: str
    mail_adr: str
    hashed_pw: Optional[str]
    salt: Optional[str]
    rfid: Optional[str]
    pin: Optional[int]


class NewUserDAO(BaseModel):
    name: str
    mail_adr: str
    password: str

    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe",
                "mail_adr": "john@test.com",
                "password": "password"
            }
        }
