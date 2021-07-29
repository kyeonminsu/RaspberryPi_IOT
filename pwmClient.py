import RPi.GPIO as IoPort
import socket
from operator import eq
import sys
import time

def sendData(x):
    send_data = '1'
    com_socket.send(bytes(send_data, "UTF-8"))

def sendData1(x):
    send_data = '2'
    com_socket.send(bytes(send_data, "UTF-8"))

def sendData2(x):
    send_data = '3'
    com_socket.send(bytes(send_data, "UTF-8"))
    
sw=4
sw1=17
sw2=27 
IoPort.setmode(IoPort.BCM)
IoPort.setup(sw, IoPort.IN)
IoPort.setup(sw1, IoPort.IN)
IoPort.setup(sw2, IoPort.IN)

print("start!!")
com_socket = socket.socket()
com_socket.connect(('192.168.0.7',3133))


IoPort.add_event_detect(sw,IoPort.FALLING,callback=sendData,bouncetime=200)
IoPort.add_event_detect(sw1,IoPort.FALLING,callback=sendData1,bouncetime=200)
IoPort.add_event_detect(sw2,IoPort.FALLING,callback=sendData2,bouncetime=200)
    
while True:
    time.sleep(1)
