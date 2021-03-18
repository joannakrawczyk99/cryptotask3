import sqlite3
import unittest

import addDb
from addHash import UserProfile

class MyTestCase(unittest.TestCase):
    def test_init_User_Profile(self):
        user = UserProfile("username", "password")
        mess = 'Given object is not instance od UserProfile'
        self.assertIsInstance(user, UserProfile, mess)

    def test_init_dbFunctions(self):
        conn = sqlite3.connect('passwords.db')
        c = conn.cursor()
        db = addDb.DbFunctions(conn, c)
        mess = 'Given object is not instance od dbFunctions'
        self.assertIsInstance(db, addDb.DbFunctions, mess)

if __name__ == '__main__':
    unittest.main()
