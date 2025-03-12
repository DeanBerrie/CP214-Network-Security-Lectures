import hashlib
import hmac
import secrets


class SecretHashFunction:
    """eudghushguerds"""

    def __init__(self, secret_key=None):
        """fusgsfdgsadhisadi"""
        self.secret_key = secret_key or secrets.token_bytes(32)

    def hash_value(self, message):
        """sgbsfgssduizhasygdygsdyfhsdyi"""
        message_bytes = message.encode('utf-8')
        hashed = hmac.new(self.secret_key, message_bytes, hashlib.sha256)
        return hashed.hexdigest()

    def verify(self, message, expected_hash):
        """osmond!!!!"""
        return hmac.compare_digest(self.hash_value(message), expected_hash)


if __name__ == '__main__':
    secret_hasher = SecretHashFunction()
    message_to_share = "Hello, world!"

    hashed_value = secret_hasher.hash_value(message_to_share)
    print(f"Message: {message_to_share}")
    print(f"Hash: {hashed_value}")

    is_valid = secret_hasher.verify(message_to_share, hashed_value)
    print(f"Verification: {is_valid}")
