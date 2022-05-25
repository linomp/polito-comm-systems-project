from pydantic.main import BaseModel
from typing import Optional

class NewCardDAO(BaseModel):
    id: int
    rfid: int
    pin: int

