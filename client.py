import socket
from operator import eq
import sys
com_socket = socket.socket()
#com_socket.connect(('192.168.0.16', 20000))
str1="Q"
com_socket.connect(('127.0.0.1', 2561))
while True:
    send_data = input("message : ")
    if(eq(str1, send_data)):
        com_socket.send(bytes(send_data, "UTF-8"))
        print("End")
        sys.exit()
    com_socket.send(bytes(send_data, "UTF-8"))
    print(com_socket.recv(4096).decode("UTF-8"))
