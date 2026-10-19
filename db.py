from model import UserData

_database : list[UserData] = [
    UserData(username='Pudge', password='zxc'),
    UserData(username='Brewmaster', password='123'),
    UserData(username='Doom', password='666'),
]

def add_user(username: str, password: str) -> str:
    existing_usernames = [user.username for user in _database]
    if username not in existing_usernames:
        user = UserData(username=username, password=password)
        _database.append(user)
        return f'{user.username} added.'
    else: return 'User already exists.'

def authenticate_user(username: str, password: str) -> bool:
    for user in _database:
        if user.username == username and user.password == password:
            return True #Todo: return JWT token
    return False



def get_all()-> list[str]:
    return [user.username for user in _database]