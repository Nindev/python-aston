'''
    Simple socket client
'''

import socket, sys, subprocess

def Connect():

    HOST = 'server'   # Symbolic name, meaning all available interfaces
    PORT = 1234 # Arbitrary non-privileged port
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    #print 'Connection established with the server on port {}'.format(PORT)

    while True:
        command = sock.recv(1024)

        if 'quit' in command:
            print 'Closing connection'
            sock.close()
            break

def Main ():

    Connect()

Main()
