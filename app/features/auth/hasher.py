from pwdlib import PasswordHash

class Hasher:
    _password_hash = PasswordHash.recommended()

    @staticmethod
    def hash(password: str) -> str:
        return Hasher._password_hash.hash(password)

    @staticmethod
    def verify(password: str, hashed_password: str) -> bool:
        return Hasher._password_hash.verify(password, hashed_password)