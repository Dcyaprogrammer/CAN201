# server side
# This implementation will have a blank xjtlu1.jpg since the 
# server continues to listen after the first transimission
# which will reopen the xjtlu1.jpg causing rewrite 

# For single time file exchange with the client one can delete
# the while loop
from socket import *

server_port = 12000
buffer_size = 65536

CHUNK_SIZE = 1024

server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(('', server_port))

print('The server is ready to receive. ')

#while True:
try:
    print("\nphase 1: waiting for xjtlu.jpg...")
    with open('xjtlu1.jpg', 'wb') as f:
        while True:
            # receive chunks
            message, client_address = server_socket.recvfrom(buffer_size)

            if message == b'END':
                break

            f.write(message)
    print(f"file xjtlu1.jpg has been recvfrom {client_address} and saved ")
    
    print("\nphase 2: sending xjtlu1.jpg back to client...")
    with open('xjtlu1.jpg', 'rb') as f: 
        while True:
            chunk = f.read(CHUNK_SIZE) #20kb
            if not chunk:
                break
            
            server_socket.sendto(chunk, client_address)
    
    server_socket.sendto(b'END', client_address)
    print("send completed")
except KeyboardInterrupt:
    print("\n Server is shutting down")
    #break
except Exception as e:
    print(f"An error occured: {e}")
        
server_socket.close()
