import unittest
from user import User


class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Caroline", "1234")

    def tearDown(self):
        """
        tearDown method that does clean up after each test case runs
        """
        User.user_names = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.user_name, "Caroline")
        self.assertEqual(self.new_user.password, "1234")

    def test_save_user(self):
        """
        test case to see if the user name is saved into the user usernames
        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_names), 1)

    def test_save_multiple_users(self):
        """
        test_save_multiple_users to check if we can save multiple usernames to our user_names
        """
        self.new_user.save_user()
        test_user = User("Mary", "1234")
        test_user.save_user()
        self.assertEqual(len(User.user_names), 2)

    def test_user_exists(self):
        """
        test to check if we can return a Boolean if we cannot find the users
        """
        self.new_user.save_user()
        test_user = User("Mary", "1234")
        test_user.save_user()

        user_exists = User.user_exist("Mary")
        self.assertTrue(user_exists)


if __name__ == '__main__':
    unittest.main()
