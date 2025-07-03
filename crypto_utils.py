# crypto_utils.py
from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def save_key(key, filename="key.key"):
    with open(filename, "wb") as key_file:
        key_file.write(key)

def load_key(filename="key.key"):
    with open(filename, "rb") as key_file:
        return key_file.read()

def encrypt_message(message, key):
    cipher = Fernet(key)
    return cipher.encrypt(message.encode())

def decrypt_message(encrypted, key):
    cipher = Fernet(key)
    return cipher.decrypt(encrypted).decode()