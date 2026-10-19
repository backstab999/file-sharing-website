import jwt, time, os
from model import UserData
from dotenv import load_dotenv


_database : list[UserData] = [
    UserData(username='Pudge', password='zxc', id = 0),
    UserData(username='Brewmaster', password='123', id = 1),
    UserData(username='Doom', password='666', id = 2),
]

def add_user(username: str, password: str) -> str:
    existing_usernames = [user.username for user in _database]
    if username not in existing_usernames:
        user_id = len(_database)
        user = UserData(username=username, password=password, id=user_id)
        _database.append(user)
        return f'{user.username} added.'
    else: return 'User already exists.'

def authenticate_user(username: str, password: str) -> bool:
    for user in _database:
        if user.username == username and user.password == password:
            #first JWT implementation
            get_jwt()
    return False


def get_jwt(username: str, password: str) -> str:
    load_dotenv()
    key = os.getenv('JWT_KEY')
    encoded=jwt.encode({'username': username, 'password': password}, key, algorithm='HS256')







def get_all()-> list[str]:
    return [user.username for user in _database]