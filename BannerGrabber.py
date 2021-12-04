import socket

# s = socket.socket()

# ip = input("Please enter your IP: ")
# port = str(input("Please enter your port: "))
# s.connect((ip, int(port)))

# print(s.recv(1024))


def banner(ip, port):
    s = socket.socket()
    s.connect((ip, int(port)))
    s.settimeout(5)
    print(s.recv(1024))


def main():
    ip = input("Please enter your IP: ")
    port = str(input("Please enter your port: "))
    banner(ip, port)


main()
