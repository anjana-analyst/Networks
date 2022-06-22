from socket import *
s = socket(AF_INET,SOCK_STREAM) 
s.bind(("127.0.0.1",8000))
s.listen(5)
while True:
    data,server = s.accept()
    print("Receieved connection from ",server)
    data1 = data.recv(100).decode()
    print(data1)
