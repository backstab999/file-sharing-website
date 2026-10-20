from dotenv import load_dotenv
from fastapi import FastAPI, Body, Depends, HTTPException, Response
from fastapi.security import HTTPBasicCredentials, HTTPBasic
from db import verify_signature, authenticate_user

servak = FastAPI()
basic = HTTPBasic()
load_dotenv()

#сырая функция авторизации, реализованная через HTTP Basic Auth
@servak.get("/auth")
def get_auth(creds:HTTPBasicCredentials = Depends(basic)):
    jwt_token = authenticate_user(creds.username,creds.password)
    if jwt_token != '':
           return jwt_token
    raise HTTPException(status_code=401, detail="Incorrect username or password")

@servak.post("/verify")
def verify(token: str = Body()):
    res = verify_signature(token)

    if res:
        return Response(status_code=200)

    return Response(status_code=400)

@servak.post("/register")
def register(username: str = Body(), password: str = Body()):
    from db import add_user
    return add_user(username, password)

@servak.get("/users")
def users():
    from db import get_all
    return get_all()


#todo:
#   прочитать внедрение зависимостей dependencies injection fastapi
#   клинап репо
#   requirements.txt
#   авторизация через обработку эндопинта через зависимости
#   restapi
#   filesharing
#   DB таблица user минимальная
#
#   service -- внутрянка - локальное хранилище для файлов
#
#   read SQL DB | db таблицы ORM + migration
#
#   async + Starlette
#   deploy CI/CD + DOCKER ( baza )
#
#