from pydantic.main import BaseModel
from typing import Optional


class Terminal(BaseModel):
    id: Optional[int]
    mac_adr: str
    cst_id: int
    pin: int