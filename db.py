import jwt, os
from datetime import datetime, timedelta, timezone
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

def authenticate_user(username: str, password: str) -> str:
    for user in _database:
        if user.username == username and user.password == password:
            return get_jwt(user.id)
    return ''


def get_jwt(id: int) -> str:
    key = os.getenv('JWT_KEY')
    now = datetime.now(timezone.utc)
    payload = {
        'sub':str(id),
        'iat':now,
        'exp':now + timedelta(minutes=3)
    }
    return jwt.encode(payload,key,algorithm='HS256')

def verify_signature(token: str) -> bool:
    key = os.getenv('JWT_KEY')
    try:
        jwt.decode(token, key, algorithms=['HS256'])
    except Exception as e:
        print(e)
        return False
    return True


def get_all()-> list[str]:
    return [user.username for user in _database]