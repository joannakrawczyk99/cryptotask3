import unittest

import addDb
from addHash import UserProfile

class MyTestCase(unittest.TestCase):
    def init_User_Profile_test(self):
        user = UserProfile()
        mess = 'Given object is not instance od UserProfile'
        self.assertIsInstance(user, addDb.dbFunctions, mess)


if __name__ == '__main__':
    unittest.main()
