# client.py
import socket
import threading
from crypto_utils import load_key, encrypt_message, decrypt_message

HOST = '127.0.0.1'
PORT = 9999
KEY = load_key()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive_messages():
    while True:
        try:
            encrypted = client.recv(2048)
            if encrypted:
                decrypted = decrypt_message(encrypted, KEY)
                print(f"\n[ENCRYPTED MESSAGE] {decrypted}\nYou: ", end="")
        except:
            print("[CONNECTION CLOSED]")
            break

threading.Thread(target=receive_messages).start()

while True:
    msg = input("You: ")
    encrypted = encrypt_message(msg, KEY)
    client.send(encrypted)