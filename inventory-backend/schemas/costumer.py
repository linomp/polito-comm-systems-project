from pydantic.main import BaseModel


class Costumer(BaseModel):
    id: int
    cst_id: int
    name: str
    category: str