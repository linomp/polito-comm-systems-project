from pydantic.main import BaseModel


class TestMessage(BaseModel):
    message: str
    timestamp: str
