import hashlib


def check_password(password: str, hashed_password: str) -> bool:
    if get_hashed_password(password) == hashed_password:
        return True
    return False


def get_hashed_password(password: str) -> str:
    return hashlib.sha256(password.encode('utf-8')).hexdigest()
