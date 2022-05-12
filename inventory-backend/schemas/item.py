from pydantic.main import BaseModel
from typing import Optional


class Item(BaseModel):
    id: int
    name: str
    description: Optional[str]
    category: str
    costumer_id: int
    rfid: Optional[int]