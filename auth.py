from dotenv import load_dotenv
from fastapi import Body, Depends, FastAPI, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from api.dependencies import token_verify
from services.service import authenticate_user, register_user

servak = FastAPI()
load_dotenv()

basic = HTTPBasic()

@servak.get("/auth/login")
def login(creds: HTTPBasicCredentials = Depends(basic)):
    return authenticate_user(creds)

@servak.post("/auth/register")
def register(username: str = Body(...), password: str = Body(...)):
    id = register_user(username, password)
    if id != None:
        return f'User {id} {username} registered successfully'
    return 'ERROR' #todo: error handler

@servak.get("/users")
def users(verify: str=Depends(token_verify)):
    from repositories.db import get_users
    try: verify
    except Exception as e:
        print(e)
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    return get_users()