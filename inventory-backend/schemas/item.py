from pydantic.main import BaseModel
from typing import Optional


class Item(BaseModel):
    id: Optional[int]
    name: str
    description: Optional[str]
    category: str
    costumer_id: int
    rfid: Optional[str]
    renter_user_id: Optional[int]

class NewItemDAO(BaseModel):
    name: str
    description: Optional[str]
    category: str
    rfid: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "name": "",
                "description":"",
                "category": "",
                "rfid": ""
            }
        }
    