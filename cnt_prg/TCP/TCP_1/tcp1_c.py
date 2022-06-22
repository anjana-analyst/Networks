from socket import *
s = socket(AF_INET,SOCK_STREAM) 
s.connect(("localhost",8000))
op='Hello'
s.send(op.encode('utf-8'))
data = s.recv(100).decode()
print(data)