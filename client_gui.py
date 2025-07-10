# client_gui.py
import socket
import threading
import tkinter as tk
from tkinter import scrolledtext
from crypto_utils import load_key, encrypt_message, decrypt_message

KEY = load_key()

def receive_messages():
    while True:
        try:
            encrypted = client.recv(2048)
            if encrypted:
                decrypted = decrypt_message(encrypted, KEY)
                chat_box.config(state='normal')
                chat_box.insert(tk.END, f"Partner: {decrypted}\n")
                chat_box.config(state='disabled')
                chat_box.see(tk.END)
        except:
            break

def send_message():
    msg = input_box.get()
    if msg:
        encrypted = encrypt_message(msg, KEY)
        client.send(encrypted)
        chat_box.config(state='normal')
        chat_box.insert(tk.END, f"You: {msg}\n")
        chat_box.config(state='disabled')
        chat_box.see(tk.END)
        input_box.delete(0, tk.END)

# GUI Setup
window = tk.Tk()
window.title("Secure Chat Client")

chat_box = scrolledtext.ScrolledText(window, state='disabled', width=60, height=20)
chat_box.pack(padx=10, pady=10)

input_box = tk.Entry(window, width=50)
input_box.pack(padx=10, pady=5)

send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack(pady=5)

# Connect to server
HOST = '127.0.0.1'
PORT = 9999
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

threading.Thread(target=receive_messages, daemon=True).start()
window.mainloop()