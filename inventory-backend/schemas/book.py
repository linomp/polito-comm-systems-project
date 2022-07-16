from pydantic.main import BaseModel
from typing import Optional


class Book(BaseModel):
    id: Optional[int]
    book_id: int
    author: str
    year: Optional[int]
    publisher: Optional[str]
    language: Optional[str]

class BookDAO(BaseModel):
    author: str
    year: Optional[int]
    publisher: Optional[str]
    language: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "author": "",
                "year": 0,
                "publisher": "",
                "language": ""
            }
        }