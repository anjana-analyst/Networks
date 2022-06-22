import os
ip=['127.0.0.1']
for ip_s in ip:
    response = os.popen(f"ping {ip}").read()
    if "Received = 4"in response:
        print(f"UP {ip} Ping Successfull")
    else:
        print(f"DOWN {ip} Ping Unsuccessful")