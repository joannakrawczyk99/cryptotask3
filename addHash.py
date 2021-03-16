import hashlib
import os

class UserProfile():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.salt = os.urandom(32)

    def getSalt(self):
        return self.salt

    def hashPassword(self, password):
        key = hashlib.pbkdf2_hmac(
            'sha256',
            str.encode(password),
            self.salt,
            100000
        )
        print(key)
        return key.hex()

