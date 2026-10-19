from fastapi import FastAPI, Body
from fastapi.responses import JSONResponse


servak = FastAPI()

@servak.post("/register")
def register(username: str = Body(), password: str = Body()):
    from db import add_user
    return add_user(username, password)

@servak.get("/users")
def users():
    from db import get_all
    return get_all()



#todo: Написать функцию, которая проверяет логин+пароль пользователя,
#      при True создает на основе его данных JWT возвращает его?
#