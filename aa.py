import random
import string

def generate_password(length=12, complexity=3):
    """
    Generates a random password.
    
    Args:
        length (int): Length of the password. Default is 12.
        complexity (int): Complexity level of the password, 1-3.
                          1: Only letters
                          2: Letters and numbers
                          3: Letters, numbers, and symbols
                          
    Returns:
        str: Generated password
    """
    
    if complexity == 1:
        characters = string.ascii_letters
    elif complexity == 2:
        characters = string.ascii_letters + string.digits
    elif complexity == 3:
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        raise ValueError("Complexity must be 1, 2, or 3.")
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage:
password_length = 16
password_complexity = 3
print("Generated password:", generate_password(password_length, password_complexity))
