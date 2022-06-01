from pydantic.main import BaseModel


class NewCardDAO(BaseModel):
    rfid: str
    pin: int
