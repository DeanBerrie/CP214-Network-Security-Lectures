import re

MINIMUM_STRING_LENGTH = 8


def check_password_properties(password):
    length = bool(len(password) >= MINIMUM_STRING_LENGTH)
    has_upper_character = bool(re.search(r'[A-Z]', password))
    has_lower_character = bool(re.search(r'[a-z]', password))
    has_number = bool(re.search(r'\d', password))
    has_symbol = bool(re.search(r'[^\w\s]', password))

    return length, has_upper_character, has_lower_character, has_number, has_symbol


def main():
    password = input("Password: ")
    length, has_upper_character, has_lower_character, has_number, has_symbol = check_password_properties(password)
    while password != "":
        if not length:
            print("Password does not meet the length requirements!")
        if not has_upper_character:
            print("Password does not have an upper case character!")
        if not has_lower_character:
            print("Password does not have a lower case character!")
        if not has_number:
            print("Password does not have a number!")
        if not has_symbol:
            print("Password does not contain a symbol!")
        password = input("Password: ")
        length, has_upper_character, has_lower_character, has_number, has_symbol = check_password_properties(password)
    with open('password.txt', 'w') as out_file:
        print(password, file=out_file)
main()
