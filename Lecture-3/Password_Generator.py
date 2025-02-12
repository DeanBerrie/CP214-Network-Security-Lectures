import random
import string


def main():
    password = []
    characters = string.printable
    password_length = random.randint(8, 20)
    for character in range(password_length):
        character = random.choice(characters)
        password.append(character)
    final_password = (''.join(password))
    print(f'your final password is {final_password}')


main()
