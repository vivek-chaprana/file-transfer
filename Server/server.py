import socket
import subprocess
import platform

HOST = '0.0.0.0'
PORT = 5555


# Function to get IP addresses of this machine, regardless of the OS 
def get_ip_addresses():
    ip_addresses = []
    try:
        system = platform.system()
        if system == 'Windows':
            ipconfig_output = subprocess.check_output(['ipconfig']).decode('utf-8', 'ignore')
            lines = ipconfig_output.split('\n')
            for line in lines:
                if 'IPv4 Address' in line:
                    ip_addresses.append(line.strip().split(':')[-1].strip())
            return ip_addresses
        else:
            ip_output = subprocess.check_output(['ifconfig']).decode('utf-8', 'ignore')
            keyword = 'inet '

        lines = ip_output.split('\n')
        for line in lines:
            if keyword in line:
                ip = line.split(keyword)[-1].split()[0]
                if '.' in ip:  # Basic validation for IPv4 address
                    ip_addresses.append(ip)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
    return ip_addresses

# Handle receiving of file from client
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

    # Get IP addresses of this machine and display them to the user
    ip_addresses = get_ip_addresses()
    print("Use one of the following IP addresses to connect to this server:")
    for ip_address in ip_addresses:
        print(ip_address)

    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)

    print("Server waiting for connection...")

    # Accept connection from client
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")

    # Receive file from client
    receive_file(client_socket)

    # Close the sockets
    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    main()
