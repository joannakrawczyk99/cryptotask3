import hashlib
import os

class UserProfile():
    """Class UserProfile is for dealing with inputs that user has entered."""
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.salt = os.urandom(32)

    def getSalt(self):
        return self.salt

    def hashPassword(self, password):
        """Hashing using pbkdf2_hmac."""
        key = hashlib.pbkdf2_hmac(
            'sha256',
            str.encode(password),
            self.salt,
            100000
        )
        return key

