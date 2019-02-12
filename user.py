import random


class User:
    """
    A class that generates new instances for users
    """
    user_list = []

    def __init__(self, user_name, password):
        """
        a method to define properties of our object
        Args:
            user_name: New user username.
            password : New user password.
        """
        self.user_name = user_name
        self.password = password

    def save_user(self):
        """
        save_user method saves user objects into the user_list
        """
        User.user_list.append(self)

    @classmethod
    # def user_exist(cls, used_name, used_password):
    #     """
    #     Method that checks if a user exists from the user_list
    #     """
    #     for user in cls.user_list:
    #         if user.user_name == user_name:
    #             return True
    #     return False
    @classmethod
    def check_user(cls, user_name, password):
        '''
        Method that checks if the name and password entered match entries in the users_list
        '''
        for user in User.user_list:
            if user.user_name == user_name and user.password == password:
                return user
            return False
