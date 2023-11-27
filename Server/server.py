import socket

HOST = '0.0.0.0'
PORT = 5555

def discover_server_ip():
    server_discovery_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_discovery_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_discovery_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    server_discovery_socket.bind(('0.0.0.0', PORT))

    print("Server waiting for discovery...")

    while True:
        data, addr = server_discovery_socket.recvfrom(1024)
        if data == b"Looking for server":
            server_discovery_socket.sendto(socket.gethostbyname(socket.gethostname()).encode(), addr)

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

    discover_server_ip()

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
