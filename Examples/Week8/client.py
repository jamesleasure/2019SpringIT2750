# client.py

import socket
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  

# 192.168.1.104 - Kelton
# 192.168.1.103 - Mike
# 192.168.1.102 - Dylan

addresses = ['192.168.1.104', '192.168.1.103', '192.168.1.102', '192.168.1.105', '127.0.0.1']
names = ['1. Kelton', '2. Mike', '3. Dylan', '4. James', '5. Localhost']
#NOTE: change the last port to the port your server is running on
ports = ['12345', '', '12346', '12347', '12347']

while(True):
    sendTo = input(f"Who would you like to send to? {names}")
    if (sendTo not in ['1', '2', '3', '4', '5']):
        continue
    port = '12345'

    sendTo = int(sendTo) - 1
    soc.connect((addresses[sendTo], int(ports[sendTo])))
    
    clients_input = input("Message to send: ")  
    soc.send(clients_input.encode("utf8")) # we must encode the string to bytes  
    result_bytes = soc.recv(4096) # the number means how the response can be in bytes  
    result_string = result_bytes.decode("utf8") # the return will be in bytes, so decode

    print("Result from server is {}".format(result_string))  