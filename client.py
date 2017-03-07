'''
    Simple socket client
'''

import socket

HOST = 'localhost'   # Symbolic name, meaning all available interfaces
PORT = 1717 # Arbitrary non-privileged port

server_cn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'

server_cn.connect((HOST, PORT))
print 'Connection established with the server on port {}'.format(PORT))

msg_to_send = b""
while msg_to_send != b"end":
    msg_to_send = input('> ')
    # Peut planter si vous tapez des caractères spéciaux
    msg_to_send = msg_to_send.encode()
    # On envoie le message
    server_cn.send(msg_to_send)
    msg_received = server_cn.recv(1717)
    print msg_received.decode()) # Là encore, peut planter s'il y a des accents

print 'Closing connection'
server_cn.close()
