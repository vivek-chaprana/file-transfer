import socket

# Client configuration
SERVER_HOST = '192.168.137.1'  # Replace with the server's IP address
SERVER_PORT = 5555

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((SERVER_HOST, SERVER_PORT))

print("Enter the path of the file you want to send: ");
file_path = input();

# file_path = 'filetosend.txt'  # Replace with the file you want to send

# Extract the file name from the file path
file_name = file_path.split('/')[-1]

# Send the file name to the server
client_socket.send(file_name.encode())

# Open and send the file in binary mode
with open(file_path, 'rb') as file:
    print(f"Sending {file_name}...")
    for data in file:
        client_socket.sendall(data)

print(f"{file_name} sent successfully!")
client_socket.close()
