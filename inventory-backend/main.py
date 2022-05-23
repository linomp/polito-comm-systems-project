from datetime import datetime

from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from dependencies import db
from schemas.test_message import TestMessage

from controllers import users

app = FastAPI()
app.include_router(users.router)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
