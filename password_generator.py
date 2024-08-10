import random
import string
def generate_password(length=12):
    """Generate a random password with the specified length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    password_length = int(input("Enter the length of the password you want to generate:"))
    generate_password = generate_password(password_length)
    print("Generated Password:", generate_password)
