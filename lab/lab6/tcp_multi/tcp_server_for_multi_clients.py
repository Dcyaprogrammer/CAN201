from socket import *
import threading

server_port = 12002
server_socket = socket(AF_INET, SOCK_STREAM)

server_socket.bind(('', server_port))
server_socket.listen(10)

print('TCP server is listening!')

records = []  # A global list to store all the records!!!

def TCP_processor(connection_socket, address):
    global records
    print(address, ' connected')
    while True:
        try:
            sentence = connection_socket.recv(20480).decode()
            if sentence == '':
                break
            print(address, ' said ', sentence)
            records.append([address, sentence])
            print(records)
            modified_message = sentence.upper()
            connection_socket.send(modified_message.encode())
        except Exception as ex:
            break
    print(address, ' disconnected')
    connection_socket.close()


while True:
    try:
        connection_socket, address = server_socket.accept()
        th = threading.Thread(target=TCP_processor, args=(connection_socket, address))
        th.start()
    except Exception as ex:
        print(ex)
