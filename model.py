from pydantic import BaseModel
import json

class UserData(BaseModel):
    username: str
    password: str
    id: int

class JWT(BaseModel):
    header:dict = ''
    payload:dict = ''
    signature:str = ''

class header(BaseModel):
    alg: str = 'HS256'
    typ: str = 'JWT'

class payload(BaseModel):
    sub: int
    exp: int
    iat: int
