import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 10000)
sock.bind(server_address)
while True:
    data, address = sock.recvfrom(4096)
    if data:
        sent = sock.sendto(data, address)
