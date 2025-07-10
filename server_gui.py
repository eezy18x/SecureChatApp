# server_gui.py
import socket
import threading
import tkinter as tk
from tkinter import scrolledtext
from crypto_utils import load_key, decrypt_message

KEY = load_key()
clients = []

def handle_client(conn, addr):
    log(f"[NEW CONNECTION] {addr} connected.")
    clients.append(conn)
    while True:
        try:
            encrypted_msg = conn.recv(2048)
            if not encrypted_msg:
                break
            log(f"[ENCRYPTED MSG RECEIVED] {encrypted_msg}")
            broadcast(encrypted_msg, conn)
        except:
            break
    log(f"[DISCONNECT] {addr} disconnected.")
    clients.remove(conn)
    conn.close()

def broadcast(encrypted_msg, sender_conn):
    for client in clients:
        if client != sender_conn:
            try:
                client.send(encrypted_msg)
            except:
                pass

def start_server():
    server.listen()
    log("[LISTENING] Server is listening...")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

def log(msg):
    log_box.config(state='normal')
    log_box.insert(tk.END, msg + "\n")
    log_box.config(state='disabled')
    log_box.see(tk.END)

# GUI Setup
window = tk.Tk()
window.title("Secure Chat Server")

log_box = scrolledtext.ScrolledText(window, state='disabled', width=60, height=20)
log_box.pack(padx=10, pady=10)

HOST = '127.0.0.1'
PORT = 9999
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

threading.Thread(target=start_server, daemon=True).start()
window.mainloop()