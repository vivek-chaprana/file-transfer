import socket
import os

SERVER_IP = '192.168.1.100'  # Replace with the server's IP address
SERVER_PORT = 5555

def send_file(file_path, client_socket):
    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)

    # Send file name to server
    client_socket.send(file_name.encode())

    # Send file size to server
    client_socket.sendall(file_size.to_bytes(8, byteorder='big'))

    # Send file in chunks
    with open(file_path, 'rb') as file:
        print(f"Sending {file_name}...")
        while True:
            data = file.read(1024)
            if not data:
                break
            client_socket.sendall(data)

    print("\nFile sent successfully!")

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_IP, SERVER_PORT))

    # File path to send
    file_path = input("Enter file path: ")
    
    send_file(file_path, client_socket)

    client_socket.close()

if __name__ == "__main__":
    main()
