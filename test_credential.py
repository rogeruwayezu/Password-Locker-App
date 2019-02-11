import unittest
from credentials import Credential


class TestCredential(unittest.TestCase):
    """
    Test class that defines test cases for the credential class behavioursself.
    Args:
        unittest.TestCase:TestCase class that helps in creating test cases
    """

    def setUp(self):
        """
        Set up method to run before each test casesself.
        """
        self.new_credential = Credential("Twitter", "carombithe", "4321")

    def tearDown(self):
        """
        tearDown method that does clean up after each test case has run.
        """

        Credential.credential_list = []

    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_credential.account_type, "Twitter")
        self.assertEqual(self.new_credential.user_name, "carombithe")
        self.assertEqual(self.new_credential.generate_password, "4321")

    def test_generate_password(self):
        """
        method that generates a password
        """
        self.assertEqual(Credential.password(), Credential.password)

    def test_save_credential(self):
        """
        test save credential test case to test if the contact object is saved into the credential_list
        """
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list), 1)

    def test_save_multiple_credentials(self):
        """
        test_save_multiple_credentials to check if it can save multiple credentials objects to our credential_list
        """
        self.new_credential.save_credential()
        test_credential = Credential("Facebook", "mumocarol", "09876")
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list), 2)

    def test_display_credentials(self):
        """
        method that returns a list of all credentials save_credential
        """
        self.assertEqual(Credential.display_credentials(),
                         Credential.credential_list)


if __name__ == '__main__':
    unittest.main()
