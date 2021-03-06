'''
    Simple socket client
'''

import socket, sys, subprocess

def Connect():

    HOST = '127.0.0.1'   # Symbolic name, meaning all available interfaces
    PORT = 1234 # Arbitrary non-privileged port
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    #print 'Connection established with the server on port {}'.format(PORT)

    while True:
        command = sock.recv(1024)

        if 'quit' in command:
            print 'Closing'
            sock.close()
            break

def Main():

    Connect()

Main()
