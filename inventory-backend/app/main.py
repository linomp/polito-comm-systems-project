from datetime import datetime

from fastapi import FastAPI

from app.mocks.core.db import database
from app.mocks.schemas.message import Message

from app.routers import users

app = FastAPI()
app.include_router(users.router)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/", tags=["hello-world"], response_model=Message)
def root():
    return Message(
        message="Hello from FastAPI + MySQL app w/o ORM",
        timestamp=datetime.now().isoformat(),
    )

# TODO: Last step of FastAPI auth - https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
