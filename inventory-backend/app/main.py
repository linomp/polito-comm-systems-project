from datetime import datetime

from fastapi import FastAPI

from app.schemas.test_message import TestMessage

from app.routers import users

app = FastAPI()
app.include_router(users.router)


# TODO: update this when we have the real DB component from Catarina's branch
# @app.on_event("startup")
# async def startup():
#     await database.connect()
#
#
# @app.on_event("shutdown")
# async def shutdown():
#     await database.disconnect()


@app.get("/", tags=["hello-world"], response_model=TestMessage)
def root():
    return TestMessage(
        message="Hello from FastAPI + MySQL app w/o ORM",
        timestamp=datetime.now().isoformat(),
    )

# TODO: Last step of FastAPI auth - https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
