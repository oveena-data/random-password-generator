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

def main():
    print("\n=== Secure Password Generator ===\n")

    # Get user preferences
    while True:
        try:
            password_length = int(input("Enter desired password length: "))
            if password_length < 1:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid positive integer for password length.")

    use_uppercase = get_boolean_input("Include uppercase letters?")
    use_numbers = get_boolean_input("Include numbers?")
    use_special_chars = get_boolean_input("Include special characters?")

    try:
        password = generate_password(
            password_length,
            use_uppercase,
            use_numbers,
            use_special_chars
        )
        print(f"\nGenerated Password: {password}\n")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()



