'''
    Simple socket client
'''

import socket

HOST = 'serveur'   # Symbolic name, meaning all available interfaces
PORT = 1717 # Arbitrary non-privileged port
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'

sock.connect((HOST, PORT))
print 'Connection established with the server on port {}'.format(PORT, HOST)

while true:
    command = sock.recv(PORT)

    if command == 'quit':
    print 'Closing connection'
    sock.close()
    break

def Main ():
    Connect()

Main()
