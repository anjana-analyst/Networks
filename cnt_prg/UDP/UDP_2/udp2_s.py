import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("127.0.0.1",8000))
while True:
    m,addr = s.recvfrom(4096)
    a={'use':'useless','fate':'die'}
    g=a[m]
    s.sendto(g,addr)