import hashlib
import os

class UserProfile:
    """
    Class UserProfile is for dealing with inputs that user has entered.
    ...
    Attributes
    ----------
    username : str
        username entered by the user
    password : str
        password entered by the user
    Methods
    -------
     hashPassword(password):
        makes hashes using pbkdf2_hmac from hashlib
    """
    def __init__(self, username, password):
        """
        Construct all the necessary attributes for the userprofile object.

        :param username: username entered by the user
        :param password: password entered by the user

        salt: str
            generating unique, random salt for the password
        """
        self.username = username
        self.password = password
        self.salt = os.urandom(32)

    def getSalt(self):
        return self.salt

    def hashPassword(self, password):
        """
        Returns hashed password and salt
        :param password: password entered by the user
        :return: hashed password
        """
        key = hashlib.pbkdf2_hmac(
            'sha256',
            str.encode(password),
            self.salt,
            100000
        )
        return key



