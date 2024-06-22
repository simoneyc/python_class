import socket
import threading

clients = {}
client_list = []
addresses = {}
game = {
    "active": False,
    "secret_number": "",
    "players": [],
    "guess_history": []
}

HOST = '127.0.0.1'
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)
running = True

def broadcast(message, prefix=""):
    for sock in clients:
        sock.send(bytes(prefix, "utf8") + message)

def handle_client(client):
    name = client.recv(1024).decode("utf8")
    welcome = f'Received: {name} join\nReceived: instructions: /exit, /search, /private, /broadcast, /play'
    client.send(bytes(welcome, "utf8"))
    msg = f'Received: {name} join'
    broadcast(bytes(msg, "utf8"))
    clients[client] = name
    print(f"{name} join")
    client_list.append(name)
    while True:
        try:
            msg = client.recv(1024)
            if msg:
                if msg == bytes("/exit", "utf8"):
                    client.send(bytes("/exit", "utf8"))
                    client.close()
                    del clients[client]
                    client_list.remove(name)
                    broadcast(bytes(f'{name} has left the chat.', "utf8"))
                    break
                elif msg == bytes("/search", "utf8"):
                    active_users = " ".join(f"{i}:{n}" for i, n in enumerate(client_list))
                    client.send(bytes(f"Received: {active_users}\nReceived: ok", "utf8"))
                elif msg == bytes("/private", "utf8"):
                    client.send(bytes("Received: target ID", "utf8"))
                    target_name = client.recv(1024).decode("utf8")
                    target_client = None
                    for cli, uname in clients.items():
                        if uname == target_name:
                            target_client = cli
                            break
                    if target_client:
                        client.send(bytes("Received: message", "utf8"))
                        private_msg = client.recv(1024).decode("utf8")
                        target_client.send(bytes(f"Received: {name}: {private_msg}", "utf8"))
                        client.send(bytes("Received: ok", "utf8"))
                    else:
                        client.send(bytes(f"User {target_name} not found.", "utf8"))
                elif msg.startswith(bytes("/broadcast", "utf8")):
                    client.send(bytes("Received: message", "utf8"))
                    broadcast_msg = client.recv(1024).decode("utf8")
                    broadcast(bytes(broadcast_msg, "utf8"), "Received: ")
                    client.send(bytes("Received: ok", "utf8"))
                elif msg.startswith(bytes("/play", "utf8")):
                    if not game["active"]:
                        if len(game["players"]) == 0:
                            client.send(bytes("Received: Answer:", "utf8"))
                            game["players"].append(client)
                        else:
                            game["players"].append(client)
                            client.send(bytes("You have joined the game. Waiting for the first player to set the secret number.", "utf8"))
                    else:
                        game["players"].append(client)
                        client.send(bytes("Received: --------------------\nstart game:", "utf8"))
                elif not game["active"] and game["players"] and game["players"][0] == client:
                    secret_number = msg.decode("utf8")
                    if len(secret_number) == 4 and len(set(secret_number)) == 4:
                        game["secret_number"] = secret_number
                        game["active"] = True
                        client.send(bytes("Received: --------------------\nstart game:", "utf8"))
                    else:
                        client.send(bytes("Invalid number. Please set a 4 unique digits number: ", "utf8"))
                elif game["active"] and client in game["players"]:
                    guess = msg.decode("utf8")
                    result = check_guess(guess, game["secret_number"])
                    game["guess_history"].append((name, guess, result))
                    broadcast(bytes(f"Received: {name}:{result}", "utf8"))
                    if result == "4A0B":
                        broadcast(bytes(f"{name} Win!", "utf8"))
                        reset_game()
                else:
                    broadcast(msg, name + ": ")
        except OSError:
            break

def check_guess(guess, secret):
    a = sum(1 for g, s in zip(guess, secret) if g == s)
    b = sum(1 for g in guess if g in secret) - a
    return f"{a}A{b}B"

def reset_game():
    game["active"] = False
    game["secret_number"] = ""
    game["players"].clear()
    game["guess_history"].clear()
    for client in clients:
        client.send(bytes("End. Type /play to start a new game.", "utf8"))

def accept_connections():
    while running:
        try:
            client, client_address = server.accept()
            # print(f"{client_address} has connected.")
            client.send(bytes("Connected to server\nReceived: User name", "utf8"))
            addresses[client] = client_address
            threading.Thread(target=handle_client, args=(client,)).start()
            print(f"Accepted connection from {client_address}")
        except OSError:
            break

def shutdown_server():
    global running
    while True:
        cmd = input()
        if cmd == "/shutdown":
            running = False
            server.close()
            print("Server is shutting down...")
            for client in clients.keys():
                client.close()
            break

if __name__ == "__main__":
    print("Server listening......")
    accept_thread = threading.Thread(target=accept_connections)
    accept_thread.start()
    shutdown_thread = threading.Thread(target=shutdown_server)
    shutdown_thread.start()
    accept_thread.join()
    shutdown_thread.join()
    print("Server has been shut down.")
