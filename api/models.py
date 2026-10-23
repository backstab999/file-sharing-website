from pydantic import BaseModel


class UserData(BaseModel):
    username: str
    hashed: str
    id: int
#todo: roles / status