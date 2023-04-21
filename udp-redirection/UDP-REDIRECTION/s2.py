# local service
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR, SOCK_DGRAM
import time
local_port = 21000
local_ip='10.0.2.4'

def server():
    server_port = local_port
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server_socket.bind(('', server_port))
    server_socket.listen(10)
    print(local_ip, 'The server is ready to receive')
    while True:
        connectionSocket, addr = server_socket.accept()
        print(addr, 'success connection')
        for i in range(5):
            msg = connectionSocket.recv(1024)
            print(msg.decode())
            mssg = 'Hi, I am Server 2'
            connectionSocket.send(mssg.encode())


def server_udp():
    server_port = local_port
    server_socket = socket(AF_INET, SOCK_DGRAM)
    server_socket.bind(('', server_port))

    print(local_ip, 'The server is ready to receive: UDP')

    while True:
        message, client_address = server_socket.recvfrom(20480)
        print (message.decode())
        #print(time.time())
        modifiedMessage = "Hello, I am Server_2"
        server_socket.sendto(modifiedMessage.encode(), client_address)


if __name__ == '__main__':
     #server();
    server_udp();
