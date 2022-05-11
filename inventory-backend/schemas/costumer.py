from pydantic.main import BaseModel


class Costumer(BaseModel):
    id: int
    name: str
    category: str