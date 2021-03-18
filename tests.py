import unittest

from addHash import UserProfile


def hashPassword():
    pass


class MyTest(unittest.TestCase):
    def hashPasswordTest(self):
        user = UserProfile("user", "password")
        self.assertTrue(hashPassword(user.password))


if __name__ == '__main__':
    unittest.main()
