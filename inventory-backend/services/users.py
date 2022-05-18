from datetime import datetime, timedelta
from typing import Optional

from fastapi import Depends, HTTPException
from starlette import status

from jose import JWTError, jwt

from dependencies import oauth2_scheme
from env import *

from schemas.Token import TokenData
from services.auth import verify_password

# TODO: replace mocks with real implementation!
from mocks.cruds.users import get_user
from mocks.schemas.user import User

from cruds import users as user_funcs
from schemas.user import User as RealDBUser


def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(token_data.username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


async def get_protected_route_example(current_user: User):
    return {"message": f"Welcome to this protected route, {current_user.full_name}"}


def test_add_user(mail):
    new_user = RealDBUser(id=None, name="Maria Margarida", mail_adr=mail,
                          hashed_pw=None, salt=None, rfid=None, pin=None)
    user_funcs.add_user(new_user, "password")

    created_user = user_funcs.get_user_from_email(mail)

    return created_user
