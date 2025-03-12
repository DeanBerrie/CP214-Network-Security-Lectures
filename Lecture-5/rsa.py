from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes


class RSASecretHash:
    def __init__(self, private_key=None):
        """
        Initializes RSA keys. If no private key is provided, a new key pair is generated.
        """

        if private_key is None:
            self.private_key = rsa.generate_private_key(
                public_exponent=65537,
                key_size=2048  # Key size can be 2048 or 4096 for better security
            )
        else:
            self.private_key = private_key
        self.public_key = self.private_key.public_key()

    def sign_message(self, message):
        """
        Signs a message using RSA and SHA-256.
        :param message: The message to sign.
        :return: The digital signature (bytes).
        """
        message_bytes = message.encode('utf-8')
        signature = self.private_key.sign(
            message_bytes,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return signature

    def verify_signature(self, message, signature):
        """
        Verifies the signature of a message using the public key.
        :param message: The original message.
        :param signature: The RSA digital signature.
        :return: True if verification is successful, False otherwise.
        """
        message_bytes = message.encode('utf-8')
        try:
            self.public_key.verify(
                signature,
                message_bytes,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except Exception:
            return False


# Example Usage
if __name__ == "__main__":
    rsa_hasher = RSASecretHash()  # Generates RSA keys
    message_to_share_to_osmond = input("Hello, hand me the goods: ")
    # Generate RSA signature
    signature_osmond = rsa_hasher.sign_message(message_to_share_to_osmond)
    print(f"Message: {message_to_share_to_osmond}")
    print(f"Signature (hex): {signature_osmond.hex()}")
    # Verification
    is_valid = rsa_hasher.verify_signature(message_to_share_to_osmond, signature_osmond)
    print(f"Verification: {is_valid}")
