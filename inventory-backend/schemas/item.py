from pydantic.main import BaseModel


class Item(BaseModel):
    id: int
    name: str
    description: str
    category: str
    costumer: int
    rfid: int