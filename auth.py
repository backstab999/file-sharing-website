from fastapi import FastAPI, Body, Depends, HTTPException
from fastapi.security import HTTPBasicCredentials, HTTPBasic

servak = FastAPI()

basic = HTTPBasic()

#сырая функция авторизации, реализованная через HTTP Basic Auth
@servak.get("/auth")
def get_auth(creds:HTTPBasicCredentials = Depends(basic)):
    from db import authenticate_user
    if not authenticate_user(creds.username,creds.password):
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    return

@servak.post("/register")
def register(username: str = Body(), password: str = Body()):
    from db import add_user
    return add_user(username, password)

@servak.get("/users")
def users():
    from db import get_all
    return get_all()
