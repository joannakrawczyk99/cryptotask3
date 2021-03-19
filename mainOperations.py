import hashlib
import logging
import addHash
import addDb
import sqlite3

def checkPasswords(pass1, pass2):
    """
    This function is to check if the user enter the same password while program asks him to do this.

    :param pass1: first password entered by the user
    :param pass2: second password entered by the user
    :return: true - if passwords are equal, false - if passwords are not equal
    """
    if (pass1 == pass2):
        return True

    else:
        return False

def verifyPassword(password, salt, key):
    """
    Function returns a messege if password verification went wrong.
    :param password: password entered by the user
    :param salt: unique, random salt for the password
    :param key: hashed password and salt
    :return: message if verification went wrong
    """
    iterations = 100000
    new = hashlib.pbkdf2_hmac(
        'sha256',
        str.encode(password),
        salt,
        iterations
    )
    if new != key:
        logging.warning('Verification failed.')
        logging.warning('Expected: ', key)
        logging.warning('Got: ', new)

if __name__ == "__main__":
    print('Enter your username: ')
    username = input()
    assert username != '', "Username should not be empty"
    print('Enter your password: ')
    password1 = input()
    assert password1 != '', "Password should not be empty"
    print('Enter your password again: ')
    password2 = input()
    assert password2 != '', "Password should not be empty"

    if checkPasswords(password1, password2):
        u1 = addHash.UserProfile(username, password1)
        key = u1.hashPassword(password1)
        salt = u1.getSalt()

        conn = sqlite3.connect('passwords.db')
        c = conn.cursor()

        db1 = addDb.DbFunctions(conn, c)
        db1.createTableIfNotExists()
        db1.insertData(username, key, salt)

        verifyPassword(password1, salt, key)

    else:
        logging.warning('Passwords are different. Try again.')
        """
        If passwords are not the same user will get a message.
        """


