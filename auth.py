from dotenv import load_dotenv
from fastapi import FastAPI, Body, Depends, HTTPException, Response

from db import verify_signature, authenticate_user

servak = FastAPI()
load_dotenv()

#region dependencies


def auth():
    return authenticate_user(creds.username, creds.password)


#endregion



#сырая функция авторизации, реализованная через HTTP Basic Auth
@servak.get("/auth")
def get_auth(jwt_token: str = Depends(auth)):
    if jwt_token != '':
           return jwt_token
    raise HTTPException(status_code=401, detail="Incorrect username or password")

#первая попытка написать авторизацию через внедрение зависимостей
@servak.get('/login')
def login():
    pass


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
#   +++++++ прочитать внедрение зависимостей dependencies injection fastapi
#   +++++++     клинап репо
#
#   авторизация через обработку эндопинта через зависимости
#   зависимость для авторизации -- db.py authenticate_user превратить в зависимость
"""
зависимость user _dep
 может получать имя и пароль пользователя из НТТР-аргументов, 
 искать их в базе данных и возвращать токен,
  применяемый для отслеживания в дальнейшем этого пользователя.
   Ваша функция веб-обработки никогда не вызывает зависимость напрямую -
    она обрабатывается во время вызова функции.
"""
#
#   requirements.txt
#   restapi
#   filesharing
#   DB таблица user минимальная
#
#   service -- внутрянка - локальное хранилище для файлов
#   read SQL DB | db таблицы ORM + migration
#
#   написание unit тестов
#   async + Starlette
#   deploy CI/CD + DOCKER ( baza )
#
#