import hashlib

import addHash
import addDb
import sqlite3


print('Enter your username: ')
username = input()
assert username != '', "Username should not be empty"
print('Enter your password: ')
password1 = input()
assert password1 != '', "Password should not be empty"
print('Enter your password again: ')
password2 = input()
assert password2 != '', "Password should not be empty"


def checkPasswords(pass1, pass2):
    """This function is to check if the user enter the same password while program asks him to do this."""
    if (pass1 == pass2):
        return True

    else:
        return False

def verifyPassword(password, salt, key):
    iterations = 100000
    new = hashlib.pbkdf2_hmac(
        'sha256',
        str.encode(password),
        salt,
        iterations
    )
    if new != key:
        print('Verification failed.')
        print('Expected: ', key)
        print('Got: ', new)


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
    print('Passwords are different. Try again.')
    """If passwords are not the same user will get a message."""


