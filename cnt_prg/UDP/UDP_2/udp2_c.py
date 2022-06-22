import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    print("Enter the word")
    w=input("-->",)
    m=str.encode(w)
    addr=("127.0.0.1",12000)
    s.sendto(m,addr)
    data,server=s.recvfrom(1024)
    print("Opposite is ",data)