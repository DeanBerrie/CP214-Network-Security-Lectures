from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad


def main():
    """DES program."""

    key = b"ANOTHER1"
    plaintext = "Hello, this is DJ Khalid speaking."
    print(f"Original plaintext: {plaintext}")

    # Encrypt
    iv, ciphertext = des_encrypt(plaintext, key)
    print(f"Encrypted with key: {ciphertext.hex()}")

    # Decrypt
    decrypted_text = des_decrypt(ciphertext, key, iv)
    print(f"Decrypted with key: {decrypted_text}")


def des_encrypt(plaintext, key):
    """Encrypt text using DES."""

    key = key[:8]
    padded_text = pad(plaintext.encode(), DES.block_size)
    cipher = DES.new(key, DES.MODE_CBC)
    ciphertext = cipher.encrypt(padded_text)

    return cipher.iv, ciphertext


def des_decrypt(ciphertext, key, iv):
    """Decrypt ciphertext using DES."""

    key = key[:8]
    cipher = DES.new(key, DES.MODE_CBC, iv)
    decrypted_text = cipher.decrypt(ciphertext)

    return unpad(decrypted_text, DES.block_size).decode()


if __name__ == '__main__':
    main()
