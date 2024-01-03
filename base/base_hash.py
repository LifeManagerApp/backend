import os
from hashlib import sha256


class Hash:
    SALT_POSTFIX = os.getenv('SALT_POSTFIX')

    @classmethod
    def hash_password(cls, password: str) -> str:
        password = f'{password}{cls.SALT_POSTFIX}'
        hash_object = sha256()
        hash_object.update(password.encode())
        return hash_object.hexdigest()
