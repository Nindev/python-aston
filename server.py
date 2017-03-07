'''
    Simple socket server
'''

import socket

HOST = 'localhost'   # Symbolic name, meaning all available interfaces
PORT = 1717 # Arbitrary non-privileged port
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'

sock.bind(('', PORT))
sock.listen(5)
print 'Socket is listenning on port '.format(PORT)

cn, addr = sock.accept()
print 'Connection at: ', addr


while true:
    command = raw_input("Enter 'quit' to exit.")

    if command == 'quit':
    print 'Closing connection'
    cn.send('quitter')
    cn.close()
    break

def Main ():
    Connect()

Main()
