
from socket import *

HOST = '192.168.24.56'
PORT = 5140
if __name__ == "__main__":
    s = socket( AF_INET, SOCK_DGRAM )
    s.bind( (HOST, PORT) )
    print '...waiting for message..'
    while True:
        data, address = s.recvfrom(1024)
        print address
    s.close()