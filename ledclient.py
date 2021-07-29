import socket
from operator import eq
import sys
com_socket = socket.socket()
str1="Q"
com_socket.connect(('127.0.0.1', 2567))
while True:
    send_data = input("message : ")
    if(eq(str1, send_data)):
        com_socket.send(bytes(send_data, "UTF-8"))
        print("End")
        com_socket.close()
        sys.exit()
    com_socket.send(bytes(send_data, "UTF-8"))
    
