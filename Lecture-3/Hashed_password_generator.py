import hashlib
import random


def main():
    password = get_password()
    salt = generate_salt()
    password_salted = f'{password}{salt}'.encode('utf-8')
    hashed_password = hashlib.sha256(password_salted).hexdigest()
    print(password)
    print(salt)
    print(hashed_password)


def generate_salt():
    salt = random.uniform(0, 10000)
    return salt


def get_password():
    with open('password.txt', 'r') as in_file:
        for line in in_file:
            password = line.strip()
    return password


main()
