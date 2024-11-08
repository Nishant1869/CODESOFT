import secrets
import string

def generate_password(length=19, min_uppercase=2, min_digits=2, min_special=2):
    # Ensure the password length is sufficient for the required minimum counts
    if length < min_uppercase + min_digits + min_special:
        raise ValueError("Password length is too short for the given requirements")

    # Define character sets for each category
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation
    
    # Ensure the password meets minimum requirements for each category
    password = [
        secrets.choice(uppercase_letters) for _ in range(min_uppercase)
    ] + [
        secrets.choice(digits) for _ in range(min_digits)
    ] + [
        secrets.choice(special_characters) for _ in range(min_special)
    ]

    # Fill the rest of the password length with random characters from all categories
    remaining_length = length - len(password)
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters
    password += [secrets.choice(all_characters) for _ in range(remaining_length)]
    
    # Shuffle the password list to ensure randomness
    secrets.SystemRandom().shuffle(password)
    
    # Convert the list into a string and return
    return ''.join(password)

# Example usage
password = generate_password(length=19, min_uppercase=3, min_digits=3, min_special=3)
print("Generated Password:", password)
