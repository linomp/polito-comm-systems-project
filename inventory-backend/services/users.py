from datetime import datetime, timedelta
from typing import Optional

from fastapi import Depends, HTTPException
from starlette import status

from jose import JWTError, jwt

from dependencies import oauth2_scheme
from env import *

from schemas.Token import TokenData
from services.auth import verify_password

from cruds import users as user_funcs
from schemas.user import User, NewUserDAO


def authenticate_user(email: str, password: str):
    user = user_funcs.get_user_from_email(email)
    if not user:
        return False
    if not verify_password(password, user.hashed_pw):
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
        mail_adr: str = payload.get("sub")
        if mail_adr is None:
            raise credentials_exception
        token_data = TokenData(mail_adr=mail_adr)
    except JWTError:
        raise credentials_exception
    user = user_funcs.get_user_from_email(token_data.mail_adr)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    return current_user


async def get_protected_route_example(current_user: User):
    return {"message": f"Welcome to this protected route, {current_user.name}"}


def add_new_user(user_data: NewUserDAO):
    new_user = User(id=None, name=user_data.name, mail_adr=user_data.mail_adr,
                    hashed_pw=None, salt=None, rfid=None, pin=None)

    user_funcs.add_user(new_user, user_data.password)

    created_user = user_funcs.get_user_from_email(user_data.mail_adr)

    return created_user
