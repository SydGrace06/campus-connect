from cryptography.fernet import Fernet
from pwdlib import PasswordHash
from pwdlib.hashers.bcrypt import BcryptHasher
from pwdlib.hashers.argon2 import Argon2Hasher
from flask_login import (
    LoginManager, login_required, login_user, logout_user, current_user
)

class UpdatedHasher:
    """Upgrades the Dropbox hasher for modern systems using Argon2 via pwdlib"""
    def __init__(self, pepper_key: bytes):
        self.pepper = Fernet(pepper_key)
        # Configure pwdlib with argon2 (rounds/time_cost can be adjusted via parameters if supported)
        self.pwd_hash = PasswordHash((Argon2Hasher(),))

    def hash(self, pwd: str) -> bytes:
        # hash with argon2
        h: str = self.pwd_hash.hash(pwd)
        # convert this unicode hash string into bytes before encryption
        hashb: bytes = h.encode('utf-8')
        # encrypt this hash using the global pepper
        pep_hash: bytes = self.pepper.encrypt(hashb)
        return pep_hash

    def check(self, pwd: str, pep_hash: bytes) -> bool:
        # decrypt the hash using the global pepper
        hashb: bytes = self.pepper.decrypt(pep_hash)
        # convert this hash back into a unicode string
        h: str = hashb.decode('utf-8')
        # check if the given password matches this hash
        return self.pwd_hash.verify(pwd, h)

    @staticmethod
    def random_pepper() -> bytes:
        return Fernet.generate_key()