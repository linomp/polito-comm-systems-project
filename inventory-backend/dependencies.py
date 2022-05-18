from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

from env import *

from components.db import DBComponent

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

db = DBComponent(host_name=DB_HOST, user_name=DB_USER, user_password=DB_PASSWORD, database=DB_NAME)
