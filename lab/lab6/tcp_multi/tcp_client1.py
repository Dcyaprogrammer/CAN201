from socket import *

server_hostname = '127.0.0.1'
server_port = 12002
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_hostname, server_port))

while True:
    sentence = input('Input a sentence')
    if sentence == '':
        break
    client_socket.send(sentence.encode())
    modified_message = client_socket.recv(20480)
    print(modified_message.decode())
client_socket.close()
