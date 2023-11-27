import socket

HOST = '0.0.0.0'
PORT = 5555

def receive_file(client_socket):
    # Receive file name from client
    file_name = client_socket.recv(1024).decode().strip()

    # Receive file size from client
    file_size_data = b''
    while len(file_size_data) < 8:
        file_size_data += client_socket.recv(8 - len(file_size_data))

    file_size = int.from_bytes(file_size_data, byteorder='big')
    received_bytes = 0

    # Open file to write
    with open(file_name, 'wb') as file:
        print(f"Receiving {file_name}...")
        while received_bytes < file_size:
            data = client_socket.recv(1024)
            received_bytes += len(data)
            file.write(data)
            # Calculate and display progress
            progress = (received_bytes / file_size) * 100
            print(f"Progress: {progress:.2f}%\r", end='')

    print("\nFile received successfully!")

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)

    print("Server waiting for connection...")

    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")

    receive_file(client_socket)

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    main()
