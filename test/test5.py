
from socket import *

HOST = '192.168.24.56'
PORT = 5140

s = socket( AF_INET, SOCK_STREAM )
s.connect( (HOST, PORT) )
while True:
    message = raw_input( 'send message:>>' )
    s.sendall( message )
    data = s.recv( 1024 )
    print data
s.close()