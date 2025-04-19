import random
import string

def generate_password(length, use_uppercase, use_numbers, use_special_chars):
    character_pool = list(string.ascii_lowercase)
    if use_uppercase:
        character_pool += list(string.ascii_uppercase)
    if use_numbers:
        character_pool += list(string.digits)
    if use_special_chars:
        character_pool += list(string.punctuation)
    
    if not character_pool:
        raise ValueError("No characyer types selected. Please choose at least one.")
    
    # Randomly select characters to form the password
    password = ''.join(random.choice(character_pool)for _ in range(length))

    return password
