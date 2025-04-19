# 🔒Random Password Generator

This is a Python-based secure password generator that allows users to create random, secure passwords based on their preferences. 

The program gives users control over the password's length and whether or not to include uppercase letters, numbers, and special characters.

<img width="1113" alt="image" src="https://github.com/user-attachments/assets/89175b5e-6d32-4cbd-9232-becd9ddef679" />


## Key Features:
- Customisable password length
- Option to include lowercase letters, uppercase letters, numbers, and special characters
- Secure password generation using Python's `random.choice()` method
- Unit tests to ensure that the password generation logic is correct

## Key Takeaways:
- Learned how to create a password generator with various customisable options based on user preferences.
- Gained experience in handling user input and validating that input.
- Implemented unit tests using Python's built-in `unittest` module to validate the password generation functionality.
- Improved knowledge of handling different types of characters and combining them in a random but secure manner.
- Understanding how to raise exceptions and handle errors gracefully when no valid character types are selected.

## How to Run the Program

```bash
    python3 main.py
 ```

The program will prompt you to enter the desired password length and select character types (lowercase, uppercase, numbers, and special characters).

Follow the on-screen prompts to generate a secure password.

## How to Run Unit Tests

1. Make sure you're in the project directory.
2. Run the following command to execute the tests:

    ```bash
    python3 -m unittest test_password_generator.py
    ```

    This will execute the test cases defined in `test_password_generator.py` and give you feedback on whether all tests pass successfully.

### Authored by Oveena Widyaratne🐍


