from api.models import UserData

#region hash
hashed1='$2b$12$4ytoi11rdI9kawTzycp0A.Jshp/kBkbjlZVsLoSrUJrElcgCMluoS'
hashed2='$2b$12$Kj1kKHkcEzD07YKwHyJeDO3PXsItUGvqF1VhNv8blbfva00KLz9SW'
hashed3='$2b$12$t2ZTBITNNk26KgNkC/CriO61XFPgbwhmhhPg97CwXNd0tyogayugq'
#endregion

#временная база данных, для удобства разработки на ранних этапах
_database : dict[str, UserData] = {
    'Pudge': UserData(username='Pudge', hashed=hashed1, id = 0), #zxc
    'Brewmaster': UserData(username='Brewmaster', hashed=hashed2, id = 1), #pivo
    'Doom': UserData(username='Doom', hashed=hashed3, id = 2), #666
}


def user_exists(username: str):
    return True

def get_user_data(username: str)-> tuple[int, str]:
    return _database[username].id, _database[username].hashed

def get_users() -> list[UserData]:
    users = [f'{u.id} {u.username}' for u in _database.values()]
    return users