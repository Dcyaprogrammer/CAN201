# client side
from socket import *

# this is only local ip 
# fo cross-host, find the real IP on each host 
server_hostname = '127.0.0.1'

server_port = 12000
buffer_size = 65536

CHUNK_SIZE = 1024

client_socket = socket(AF_INET, SOCK_DGRAM)
server_address = (server_hostname, server_port)

print("phase 1: sending xjtlu.jpg...")
try:
    with open('xjtlu.jpg', 'rb') as f:
        while True:
            chunk = f.read(CHUNK_SIZE) 
            if not chunk:
                break

            client_socket.sendto(chunk, server_address)

    client_socket.sendto(b'END', server_address)
    print("send xjtlu.jpg completed")

    print("phase 2: waiting to receive xjtlu2.jpg...")
    with open('xjtlu2.jpg', 'wb') as f:
        while True:
            modified_message, _ = client_socket.recvfrom(buffer_size)

            if modified_message == b'END':
                break
            
            f.write(modified_message)

    print("file xjtlu2.jpg has been received and saved")
except FileNotFoundError:
    print("Error: make sure xjtlu.jpg is in the same root dir with this file")
finally:
    client_socket.close()



