import addHash
import addDb
import sqlite3

print('Enter your username: ')
username = input()
print('Enter your password: ')
password1 = input()
print('Enter your password again: ')
password2 = input()

if(password1 == password2):
    u1 = addHash.UserProfile(username, password1)
    key = u1.hashPassword(password1)

    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()

    db1 = addDb.dbFunctions(conn, c)
    # db1.createTable()
    db1.insertData(username, key, u1.getSalt())

else:
    print('Passwords are different. Try again.')
