import RPi.GPIO as IoPort
import socket
from operator import eq
import sys
import time

def sendData(x):
    send_data = '1'
    com_socket.send(bytes(send_data, "UTF-8"))
    
sw=4 
IoPort.setmode(IoPort.BCM)
IoPort.setup(sw, IoPort.IN)

print("start!!")
com_socket = socket.socket()
com_socket.connect(('192.168.0.7',3139))

#while True:
    #rcv=IoPort.input(sw)
IoPort.add_event_detect(sw,IoPort.FALLING,callback=sendData,bouncetime=200)
    
while True:
    time.sleep(1)
