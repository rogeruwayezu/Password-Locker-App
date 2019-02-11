#!/usr/bin/env python3.6
from user import User
from credentials import Credential
import random


def create_user(user_name, password):
    """
    Function to create a new users
    """
    new_user = User(user_name, password)
    return new_user


def save_user(user):
    """
    Function to save contact
    """
    user.save_user()


def check_existing_users(user_name):
    """
    Functionto to check if an user exists using the user _name
    """
    return User.user_exist(user_name)


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
    Function that returns all the saved credentials
    """
    return Credential.display_credentials()


def main():
    print("Welcome!")

    print("Please enter one of the following codes to proceed, create - create user if you don't have account yet , login -if you already have an account and exit to exit the application ")
    short_code = input().lower()

    if short_code == 'create':
        print("Create user")
        print("Username")
        user_name = input()
        print("password")
        password = input()

        save_user(create_user(user_name, password))
        print('\n')
        print(f"Log in details for {user_name}  have been saved")
        print('\n')

        print("Please exit the application to log in to see your credentials")

    elif short_code == 'login':

        print("Fill in the required details")
        print("Enter your user name")
        user_name = input()
        print("Enter your password")
        password = input()

        sign_in = check_existing_users(user_name)

        if sign_in == True:
            print("welcome back")

        while True:

            print("Welcome")

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
                    "You can choose to create your password or generate it ,if you want to generate  password type generate or if create type c")
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
                print("Exiting the password locker")
                break

            else:

                print("Please use a valid code")


if __name__ == '__main__':

    main()
