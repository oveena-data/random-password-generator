import random
import string

def generate_password(length, use_lowercase, use_uppercase, use_numbers, use_special_chars):
    """
    Generate a random password based on user preferences.
    """
    character_set = []

    if use_lowercase:
        character_set += list(string.ascii_lowercase)

    if use_uppercase:
        character_set += list(string.ascii_uppercase)
    if use_numbers:
        character_set += list(string.digits)
    if use_special_chars:
        character_set += list('!@#$%^&*()-_=+[{]};:\'",<.>/?`~')

    if not character_set:
        raise ValueError("At least one character type must be selected.")

    return ''.join(random.choice(character_set) for _ in range(length))
