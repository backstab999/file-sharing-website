from model import UserData

_database : list[UserData] = []


def add_user(username: str, password: str) -> str:
    existing_usernames = [user.username for user in _database]
    if username not in existing_usernames:
        user = UserData(username=username, password=password)
        _database.append(user)
        return f'{user.username} added.'
    else: return 'User already exists.'

def get_all()-> list[str]:
    return [user.username for user in _database]