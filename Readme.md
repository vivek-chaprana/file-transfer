# File Transfer over network using Python

## Description

This is a simple file transfer program written in Python. It uses the socket library to transfer files over the network. The program is written in python.

## Getting Started

### Pre-requisites and Local Development

1. Python 3.7
2. [PIP](https://pypi.org/project/pip/)
3. [Git](https://git-scm.com/downloads)

### Installation

1. Clone the repository

```bash
git clone https://github.com/vivek-chaprana/file-transfer.git
```

2. Change directory to file-transfer

```bash
cd file-transfer
```

3. Run the application

- For server side

```bash
python3 server.py
```

- For client side

```bash
python3 client.py
```

### Usage

1. Connect to the Network:

- Ensure both the server and client machines are connected to the same local network (Wi-Fi or LAN).

2. Run the Server Script:

- On the machine intended to act as the server:
- Execute the server.py script.
- The server script will start listening for incoming connections.

3. Run the Client Script:

- On the machine intended to act as the client:
- Execute the client.py script.
- When prompted, enter the IP address provided by the server.py script.

4. Enter File Path:

- Once connected, the client will prompt for the file path to be transferred.
- Enter the full file path of the file you want to send to the server.

5. File Transfer:

- The file will be transferred to the server over the network.
- Progress of the file transfer will be displayed on both client and server sides.

6. Completion:

- Once the transfer is complete, the client and server scripts will display a success message.
- The transferred file will be saved on the server side.

7. Verify:

- Check the server-side directory to ensure the transferred file exists and is complete.

8. Done!

- The file transfer process is completed successfully. You've now transferred a file from the client to the server over the local network.
