from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status
from cruds.users import update_users_card

from schemas.Token import Token
from schemas.user import User, NewUserDAO
from schemas.card import NewCardDAO
from services.users import *

from env import ACCESS_TOKEN_EXPIRE_MINUTES

router = APIRouter()


@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.mail_adr}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user


@router.get("/users/protected/")
async def protected_route_example(current_user: User = Depends(get_current_active_user)):
    msg = await get_protected_route_example(current_user)
    return msg


@router.post("/users", tags=["test-db"])
def add_user(user_data: NewUserDAO):
    created_user = add_new_user(user_data)

    return created_user


@router.post("/users/card", tags=["test-db"])
def updt_card(card_data: NewCardDAO):
    user = updt_users_card(card_data.id, card_data)

    return user