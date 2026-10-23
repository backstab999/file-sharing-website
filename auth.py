from dotenv import load_dotenv
from fastapi import Body, Depends, FastAPI, HTTPException, Response
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from api.dependencies import token_verify
from services.service import authenticate_user, register_user

servak = FastAPI()
load_dotenv()

basic = HTTPBasic()

@servak.get("/auth/login")
def login(creds: HTTPBasicCredentials = Depends(basic)):
    jwt = authenticate_user(creds)
    if jwt is None:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    return {"access_token": jwt, "token_type": "bearer"}

@servak.post("/auth/register", status_code=201)
def register(username: str = Body(...), password: str = Body(...)):
    id = register_user(username, password)
    if id is None:
        raise HTTPException(status_code=409,detail="Username already taken")
    return f'User {id} {username} registered successfully'

@servak.get("/users", status_code=200)
def users(verify: str=Depends(token_verify)):
    from repositories.db import get_users
    try: verify
    except Exception as e:
        print(e)
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    return get_users()