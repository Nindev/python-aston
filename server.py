'''
    Simple socket server
'''

import socket

HOST = 'localhost'   # Symbolic name, meaning all available interfaces
PORT = 1717 # Arbitrary non-privileged port

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'

socket.bind((HOST, PORT))
socket.listen(5)
print 'Socket is listenning on port {}'.format(PORT))

clt, infos = socket.accept()

msg_received = b""
while msg_received != b"end":
    msg_received = clt.recv(1717)
    # L'instruction ci-dessous peut lever une exception si le message
    # Réceptionné comporte des accents
    print(msg.decode())
    clt.send(b"5/5")

print 'Closing connection'
clt.close()
socket.close()
