import os
ip=['127.0.0.1']
for ip_s in ip:
    response = os.popen(f"ping {ip_s}").read()
    if "Received = 4"in response:
        print(f"UP {ip_s} Ping Successfull")
    else:
        print(f"DOWN {ip_s} Ping Unsuccessful")
