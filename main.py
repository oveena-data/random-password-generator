from password_generator import generate_password

def main():
    print("=== Secure Password Generator ===")
    
    # Get user input for the password preferences
    length = int(input("Enter desired password length: "))
    
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    # Generate the password with the selected preferences
    try:
        password = generate_password(
            length,
            use_lowercase,
            use_uppercase,
            use_numbers,
            use_special_chars
        )
        print(f"Your secure password is: {password}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
