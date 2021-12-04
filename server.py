# steps to creat a TCP server using python
import socket

# Creating the socket object
serversocket = socket.socket(
    socket.AF_INET,  # socket family
    socket.SOCK_STREAM  # socket type
)

host = socket.gethostname()  # this will get the ip address of the server
port = 444

# binding to socket
serversocket.bind((host, port))

# starting TCP listener
serversocket.listen(3)

while True:
    # starting the connection
    clientsocket, address = serversocket.accept()
    print("received connection from " % str(address))

    message = 'Thank you for connecting to the server' + "\r\n"
    clientsocket.send(message.encode('ascii'))

    clientsocket.close()
