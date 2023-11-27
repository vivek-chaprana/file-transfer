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

    ## Receive file name from client
    file_name = client_socket.recv(1024).decode().strip()
    
    # Receive file size from client
    file_size = int(client_socket.recv(1024).decode())
    
    # Open the file received from the client in binary mode
    received_bytes = 0
    with open(file_name, 'wb') as file:
        print(f"Receiving {file_name}...")
        while received_bytes < file_size:
            # Receive file data in chunks
            data = client_socket.recv(1024)
            received_bytes += len(data)
            file.write(data)
            # Calculate and display progress
            progress = (received_bytes / file_size) * 100
            print(f"Progress: {progress:.2f}%\r", end='')
        print("\nFile received successfully!")
    client_socket.close()
