import socket
import os
import time

SERVER_PORT = 5555

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

    # Get the IP address of the server from the user
    server_ip = input("Enter IP address from server side: ")

    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, SERVER_PORT))

    # File path to send
    file_path = input("Enter file path: ")

    # Send file to server
    send_file(file_path, client_socket)

    # Close the socket
    client_socket.close()

if __name__ == "__main__":
    main()
