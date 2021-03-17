import sqlite3

import addHash
from addDb import dbFunctions
from main import username

conn = sqlite3.connect('passwords.db')
c = conn.cursor()

def createTableTest():
    db = dbFunctions(conn, c)
    db.createTable()
    c.execute('''SELECT count(*) FROM sqlite_master WHERE type='table' AND name='passwords' ''')
    assert c.fetchone()[0] == 1

def insertDataTest():
    db = dbFunctions(conn, c)
    u = addHash.UserProfile("username", "password1")
    key = u.hashPassword("password1")
    db.insertData(u.username, key, u.getSalt())
    assert db.showEverything() != 0