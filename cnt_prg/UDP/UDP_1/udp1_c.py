import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 10000)
message = 'This is the message.  It will be repeated.'
sent = sock.sendto(message.encode(), server_address)
data, server = sock.recvfrom(4096)
print(data)