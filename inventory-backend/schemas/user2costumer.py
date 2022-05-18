from pydantic.main import BaseModel
from typing import Optional


class User2Costumer(BaseModel):
    id: int
    user_id: int
    cst_id: int
    role: Optional[str]