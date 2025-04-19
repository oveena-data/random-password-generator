# main.py
from password_generator import generate_password

def get_boolean_input(prompt):
    """
    Helper function to get a yes/no response from the user and return it as a boolean.
    """
    while True:
        response = input(prompt + " (y/n): ").strip().lower()
        if response in ['y', 'yes']:
            return True
        elif response in ['n', 'no']:
            return False
        else:
            print("Please enter 'y' or 'n'.")

