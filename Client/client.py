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


# Get the size of the file
file_size = os.path.getsize(file_path)

# Send the file size to the server
client_socket.send(str(file_size).encode())

# Open and send the file in binary mode while displaying progress
sent_bytes = 0
with open(file_path, 'rb') as file:
    print(f"Sending {file_name}...")
    for data in file:
        client_socket.sendall(data)
        sent_bytes += len(data)
        # Calculate and display progress
        progress = (sent_bytes / file_size) * 100
        print(f"Progress: {progress:.2f}%\r", end='')
    print("\nFile sent successfully!")
client_socket.close()
