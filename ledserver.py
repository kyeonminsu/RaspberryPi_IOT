import socket
from operator import eq
import sys
import RPi.GPIO as IoPort
import time

IoPort.setmode(IoPort.BCM)
IoPort.setup(4, IoPort.OUT)
IoPort.setup(17, IoPort.OUT)
IoPort.setup(27, IoPort.OUT)
IoPort.setup(22, IoPort.OUT)

print("start!!")
str1='Q'
arr=['1','2','3','4']
arr2=[4,17,27,22]
i=0
com_socket=socket.socket()
com_socket.bind(('192.168.0.7',2569))
com_socket.listen(10)
connection, address = com_socket.accept()
print(address, "Connected good")
while True:
    led=connection.recv(4096).decode("UTF-8")
    print(led)
    if(eq(str1,led)):
        print("End")
        connection.close()
        sys.exit()
    for i in  range(4):
        if(eq(arr[i], led)):
            IoPort.output(arr2[i], True)
            time.sleep(1)
            IoPort.output(arr2[i], False)
