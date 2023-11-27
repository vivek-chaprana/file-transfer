import socket

# Server configuration
HOST = '0.0.0.0'  # All available interfaces
PORT = 5555

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the host and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen(1)

print(f"Server listening on port {PORT}...")

while True:
    # Accept incoming connection
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")

    # Receive file name from client
    # file_name = client_socket.recv(1024).decode()
    file_name = client_socket.recv(1024).decode().strip()

    # Open the file received from the client in binary mode
    with open(file_name, 'wb') as file:
        print(f"Receiving {file_name}...")
        while True:
            # Receive file data in chunks
            data = client_socket.recv(1024)
            if not data:
                break
            file.write(data)

    print(f"{file_name} received successfully!")
    client_socket.close()
