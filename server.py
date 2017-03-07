'''
    Simple socket server
'''

import socket, sys, subprocess

def Connect():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 1234))
    sock.listen(5)

    print 'Socket is listenning on port 1234'
    cn, addr = sock.accept()
    print 'Connection at: ', addr


    while True:
        command = raw_input("Enter 'quit' to exit\n>")

        if command == 'quit':
            print 'Closing connection'
            cn.send('quitter')
            cn.close()
            break

def Main ():
    Connect()

Main()
