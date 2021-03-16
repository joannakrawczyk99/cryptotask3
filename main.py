import addHash
import addDb
import sqlite3

print('Enter your username: ')
username = input()
print('Enter your password: ')
password = input()

u1 = addHash.UserProfile(username, password)
key = u1.hashPassword(password)

conn = sqlite3.connect('passwords.db')
c = conn.cursor()

db1 = addDb.DatabaseController(conn, c)
#db1.createTable()
db1.insertData(username, key, u1.getSalt())