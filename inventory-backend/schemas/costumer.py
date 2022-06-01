from pydantic.main import BaseModel
from typing import Optional

from schemas.user import NewUserDAO


class Costumer(BaseModel):
    id: Optional[int]
    name: str
    category: Optional[str]


class NewCostumerDAO(BaseModel):
    id: Optional[int]
    name: str
    category: Optional[str]
    default_user: Optional[NewUserDAO]
