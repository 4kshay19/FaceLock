from cryptography.fernet import Fernet
import os

KEY_FILE = "encryption/secret.key"


def load_key():
    """Load the existing encryption key."""

    if not os.path.exists(KEY_FILE):
        raise FileNotFoundError("Encryption key not found.")

    with open(KEY_FILE, "rb") as key_file:
        return key_file.read()


def decrypt_file(input_file, output_file):
    """Decrypt an encrypted file."""

    key = load_key()
    cipher = Fernet(key)

    # Read encrypted file
    with open(input_file, "rb") as file:
        encrypted_data = file.read()

    # Decrypt data
    decrypted_data = cipher.decrypt(encrypted_data)

    # Save decrypted file
    with open(output_file, "wb") as file:
        file.write(decrypted_data)

    return True