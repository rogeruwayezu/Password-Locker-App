#!/usr/bin/env python3.6
from user import User
from credentials import Credential
import random


def create_user(user_name, password):
    """
    function to create a new user
    """
    new_user = User(user_name, password)
    return new_user


def save_user(user):
    """
    Function to save user
    """
    user.save_user()


def verify_user(first_name, password):
    '''
    Function that verifies the existance of the user before creating credentials
    '''
    checking_user = User.check_user(first_name, password)
    return checking_user


def add_credential(account_type, user_name, password):
    """
    Function to add credential
    """
    new_credential = Credential(account_type, user_name, password)
    return new_credential


def save_credentials(credential):
    """
    Function to save credentials
    """
    credential.save_credential()


def display_credentials():
    """
    Function for returning all the saved credentials
    """
    return Credential.display_credentials()


# def display_credentials(user_name):
#     '''
#     Function to display credentials saved by a user
#     '''
#     return Credential.display_credentials(user_name)


def main():
    print("Welcome!")

    print("if you don't have an account yet, type ca or if you have an account type li")
    short_code = input().lower()

    if short_code == 'ca':
        print("Create user")
        print("Username")
        user_name = input()
        print("password")
        password = input()

        save_user(create_user(user_name, password))
        print('\n')
        print(f"Log in details for {user_name}  have been saved")
        print('\n')
        while True:

            print("Please exit the application to log in to see your credentials")
            short_code = input().lower()
            if short_code == 'ex':
                print("Bye ......")
                break
    elif short_code == 'li':

        print("Enter your user name")
        user_name = input()
        print("Enter your password")
        password = input()

        # sign_in = verify_user(user_name, password)

        # if sign_in == True:
        #     print("welcome back")

        while True:

            print("Welcome back")

            print("Please use these short codes to navigate: ac -add credentials, dc -display credentials, ex -exit the application")
            short_code = input().lower()
            if short_code == 'ac':
                print("Add credentials")
                print("-"*5)
                print("Account type...")
                account_type = input()
                print("User name..")
                user_name = input()
                # print("Password,,")
                # password=input()

                print(
                    "if you want to generate  password type generate or if you want to create it type create")
                code = input().lower()

                if code == 'create':
                    print("Enter your Password")
                    password = input()

                    # print(f"Password: {Credential.password}"

                elif code == 'generate':
                    s = "abcdefghijklmnopqrstuvwxyz0123456789"
                    password = ''.join(random.choice(s) for _ in range(8))

                else:
                    print("Put a valid code")

                save_credentials(add_credential(
                    account_type, user_name, password))
                print('\n')
                print(
                    f"Credentials Account {account_type} account's username {user_name} with password {password} added")
                print('\n')
            elif short_code == 'dc':
                if display_credentials():
                    print("Here is a list of your credentials")
                    print('\n')

                    for credential in display_credentials():
                        print(
                            f"{credential.account_type}..{credential.user_name} ..{credential.password}")
                        print('\n')
                else:
                    print('\n')
                    print("You don't have credentials saved yet")

            elif short_code == 'ex':
                print("Bye ......")
                break

            else:

                print("Please use a valid code")


if __name__ == '__main__':
    main()
