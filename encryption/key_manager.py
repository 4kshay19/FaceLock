from cryptography.fernet import Fernet
import os


KEY_FILE = "encryption/secret.key"


def generate_key():
    """Generate and save an encryption key."""

    os.makedirs("encryption", exist_ok=True)

    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()

        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)

        print("Encryption key created.")


def load_key():
    """Load the existing encryption key."""

    if not os.path.exists(KEY_FILE):
        generate_key()

    with open(KEY_FILE, "rb") as key_file:
        return key_file.read()


def encrypt_file(input_file, output_file):
    """Encrypt a file."""

    key = load_key()
    cipher = Fernet(key)

    with open(input_file, "rb") as file:
        file_data = file.read()

    encrypted_data = cipher.encrypt(file_data)

    with open(output_file, "wb") as file:
        file.write(encrypted_data)

    return True