from pydantic.main import BaseModel
from typing import Optional


class Costumer(BaseModel):
    id: Optional[int]
    name: str
    category: Optional[str]