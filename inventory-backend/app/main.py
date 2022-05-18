from datetime import datetime

from fastapi import FastAPI

from app.dependencies import db
from app.schemas.test_message import TestMessage

from app.routers import users

app = FastAPI()
app.include_router(users.router)


# TODO: update this when we have the real DB component from Catarina's branch
@app.on_event("startup")
def startup():
    db.create_connection()


@app.on_event("shutdown")
def shutdown():
    db.close_connection()


@app.get("/", tags=["hello-world"], response_model=TestMessage)
def root():
    return TestMessage(
        message="Hello from FastAPI + MySQL app w/o ORM",
        timestamp=datetime.now().isoformat(),
    )
