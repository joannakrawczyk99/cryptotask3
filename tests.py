import unittest

import addDb
from addHash import UserProfile

class MyTestCase(unittest.TestCase):
    def test_init_User_Profile(self):
        user = UserProfile("username", "password")
        mess = 'Given object is not instance od UserProfile'
        self.assertIsInstance(user, UserProfile, mess)


if __name__ == '__main__':
    unittest.main()
