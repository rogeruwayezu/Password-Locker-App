import random


class Credential:
    """
    Class that generates new instances of Credential
    """

    def __init__(self, account_type, user_name, password):
        """
        __init__ method that helps us define properties of our objects
             Args:
        account_type:The type of account_type
        user_name:The username for that account .
        password:password for that account.

        self variable represents the instance of the object
        """
        self.account_type = account_type
        self.user_name = user_name
        self.password = password

    credential_list = []

    def generate_password(self):
        """
        A method to generate a credential generate_password
        """
        s = "abcdefghijklmnopqrstuvwxyz0123456789"
        gen_pass = ''.join(random.choice(s) for _ in range(8))
        return gen_pass

    def save_credential(self):
        """
        save_credential method saves credential objects into the credential_list
        """
        Credential.credential_list.append(self)

    @classmethod
    def display_credentials(cls):
        """
        method that  returns the credential list
        """
        return cls.credential_list
