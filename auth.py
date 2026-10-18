from fastapi import FastAPI, Body

servak = FastAPI()

# @servak.post("/login")
# def login(username: str = Body(), password: str = Body()):
#     if auth(username, password):
#         return True
#     else:
#         return False

@servak.post("/register")
def register(username: str = Body(), password: str = Body()):
    from db import add_user
    return add_user(username, password)

@servak.get("/users")
def users():
    from db import get_all
    return get_all()

# def auth(username: str, password: str) -> bool:
#     return True