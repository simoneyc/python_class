import socket
import threading
import sys

HOST = '127.0.0.1'
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive():
    while True:
        try:
            msg = client.recv(1024).decode("utf8")
            if msg == "/exit":
                client.close()
                break
            print(msg)
        except OSError:
            break

def send():
    while True:
        msg = input()
        client.send(bytes(msg, "utf8"))
        if msg == "/exit":
            break

if __name__ == "__main__":
    receive_thread = threading.Thread(target=receive)
    receive_thread.start()
    send_thread = threading.Thread(target=send)
    send_thread.start()
    receive_thread.join()
    send_thread.join()
