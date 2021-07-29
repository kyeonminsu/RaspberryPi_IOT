import socket
from operator import eq
import sys
com_socket=socket.socket()
com_socket.bind(('127.0.0.1',2561))
#com_socket.bind(('192.168.0.11',2567))
str1="Q"
com_socket.listen(10)
connection, address = com_socket.accept()
print(address, "Connected good")
while True:
    send_data=connection.recv(4096).decode("UTF-8")
    if(eq(str1,send_data)):
        print("client end -> server end")
        sys.exit()
    connection.send(bytes(send_data, "UTF-8"))


