import string
from random import choice

def generate_secret_key(length=50):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(choice(characters) for _ in range(length))

if __name__ == "__main__":
    secret_key = generate_secret_key()
    print(f'SECRET_KEY={secret_key}')
