from fastapi import Header
import os, jwt


def token_verify(token: str = Header()):
    key = os.getenv('JWT_KEY')
    try:
        jwt.decode(token, key, algorithms=["HS256"])
    except Exception as e:
        print(e)
        return False
    return True
