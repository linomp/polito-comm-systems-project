from fastapi import FastAPI
from .routers import items
from app.core.db import database

app = FastAPI()
app.include_router(items.router)
sleep_time = 10


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/")
def root():
    return {
        "message": "Hello from FastAPI + MySQL app w/o ORM",
        "hint": "Try this endpoint:  http://localhost:8000/items/"
    }
