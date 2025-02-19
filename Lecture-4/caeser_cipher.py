def main():
    password = get_password()
    shift = 4
    ciphertext = ""
    for ch in password:
        if ch.isalpha():
            stay_in_alphabet = ord(ch) + shift
            if stay_in_alphabet > ord('z'):
                stay_in_alphabet -= 26
            final_letter = chr(stay_in_alphabet)
            ciphertext += final_letter
    print(password)
    print(ciphertext)


def get_password():
    with open('../Lecture-3/password.txt', 'r') as in_file:
        for line in in_file:
            password = line.strip()
    return password


main()
