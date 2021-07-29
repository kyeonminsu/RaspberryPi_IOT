import socket
from operator import eq
import sys
import RPi.GPIO as IoPort
import time

IoPort.setmode(IoPort.BCM)
IoPort.setup(17, IoPort.OUT)
print("start!!")
com_socket=socket.socket()
com_socket.bind(('192.168.0.7',3139))
com_socket.listen(10)
connection, address = com_socket.accept()
print(address, "Connected good")
i=0
while True:
    led=connection.recv(4096).decode("UTF-8")
    print(led)
    if(i==0):
        if(led=='1'):
            IoPort.output(17, True)
            i=1

    elif(i==1):
        if(led=='1'):
            IoPort.output(17, False)
            i=0
