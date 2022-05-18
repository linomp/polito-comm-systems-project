from typing import Optional

from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    mail_adr: Optional[str] = None
    # TODO: add here other fields like Role, "Customer"
