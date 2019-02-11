class User:
    """
    A class that generates new instances for users
    """

    def __init__(self, user_name, password):
        """
        a method to define properties of our object
        Args:
            user_name: New user username.
            password : New user password.
        """
        self.user_name = user_name
        self.password = password
    user_names = []

    def save_user(self):
        """
        save_user method saves user objects into the user_names
        """
        User.user_names.append(self)

    @classmethod
    def user_exist(cls, user_name):
        """
        Method that checks if a user exists from the user_names
        """
        for user in cls.user_names:
            if user.user_name == user_name:
                return True

        return False
