import os
from datetime import UTC, datetime, timedelta, timezone

import bcrypt
import jwt

from repositories.db import get_user_data, user_exists, user_create


#сюда позже должны передаваться еще и статус + роль пользователя для авторизации в jwt после ответа от БД
def authenticate_user(username: str, password: str) -> str | None:
    user_id, hashed_password = get_user_data(username)
    if user_id is None or hashed_password is None:
        return None
    if verify_password(hashed_password, password):
        return get_jwt(user_id)

def register_user(username: str, password: str)-> int | None:
    #todo: validate_username && validate_password
    if user_exists(username):
        return None
    hashed_password = get_hashed_password(password)
    user_id = user_create(username, hashed_password)
    return user_id

#добавить в payload роль и статус пользователя для прав (авторизации)
def get_jwt(user_id: int) -> str:
    key = os.getenv('JWT_KEY')
    now = datetime.now(UTC)
    payload = {
        'sub':str(user_id),
        'iat':now,
        'exp':now + timedelta(minutes=3)
    }
    return jwt.encode(payload,key,algorithm='HS256')

def get_hashed_password(password: str, round: int = 12) -> str:
    salt = bcrypt.gensalt(round)
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def verify_password(hashed: str, password: str) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))