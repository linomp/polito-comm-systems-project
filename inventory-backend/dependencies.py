from fastapi.security import OAuth2PasswordBearer

from env import *

from components.db import DBComponent

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

db = DBComponent(host_name=DB_HOST, user_name=DB_USER, user_password=DB_PASSWORD, database=DB_NAME)
