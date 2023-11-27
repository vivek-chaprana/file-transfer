import socket
import os
import time

# SERVER_IP = '192.168.1.9'  # Replace with the server's IP address
# SERVER_PORT = 5555

SERVER_PORT = 5555
CLIENT_PORT = 5556  # Client's listening port for server discovery
CLIENT_BROADCAST_IP = '255.255.255.255'  # Broadcast address

def discover_server_ip():
    client_discovery_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_discovery_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    client_discovery_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    client_discovery_socket.bind(('0.0.0.0', CLIENT_PORT))

    # Send a broadcast message for server discovery
    client_discovery_socket.sendto(b"Looking for server", (CLIENT_BROADCAST_IP, SERVER_PORT))

    print("Looking for server...")
    time.sleep(2)  # Wait for a response

    # Receive server's IP address from broadcast response
    data, _ = client_discovery_socket.recvfrom(1024)
    server_ip = data.decode()

    print(f"Server found at {server_ip}")
    client_discovery_socket.close()
    return server_ip

def send_file(file_path, client_socket):
    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)

    # Send file name to server
    client_socket.send(file_name.encode())

    # Send file size to server
    client_socket.sendall(file_size.to_bytes(8, byteorder='big'))

    # Send file in chunks with progress indication
    sent_bytes = 0
    with open(file_path, 'rb') as file:
        print(f"Sending {file_name}...")
        while True:
            data = file.read(1024)
            if not data:
                break
            client_socket.sendall(data)
            sent_bytes += len(data)
            # Calculate and display progress
            progress = (sent_bytes / file_size) * 100
            print(f"Progress: {progress:.2f}%\r", end='')

    print("\nFile sent successfully!")

def main():
    server_ip = discover_server_ip()

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, SERVER_PORT))

    # File path to send
    file_path = input("Enter file path: ")

    send_file(file_path, server_ip, client_socket)

    client_socket.close()

if __name__ == "__main__":
    main()
