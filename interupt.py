import RPi.GPIO as IoPort
import time
sw=4
sw1=23
IoPort.setmode(IoPort.BCM)
IoPort.setup(22, IoPort.OUT)
IoPort.setup(17, IoPort.OUT)
IoPort.setup(27, IoPort.OUT)
IoPort.setup(18, IoPort.OUT)
IoPort.setup(sw, IoPort.IN)
IoPort.setup(sw1, IoPort.IN)
arr=[22,17,27,18]

def wow():
    for i in range (0, 4):
            IoPort.output(arr[i], True)
            time.sleep(0.5)
            IoPort.output(arr[i], False)
            time.sleep(0.5)
     
def wow1():
    i=3
    while(i>=0):
        IoPort.output(arr[i], True)
        time.sleep(0.5)
        IoPort.output(arr[i], False)
        time.sleep(0.5)
        i=i-1
    
while True:
    rcv=IoPort.input(sw)
    rcv=IoPort.input(sw1)
     
IoPort.add_event_detect(sw,IoPort.FALLING,callback=wow,bouncetime=200)
IoPort.add_event_detect(sw1,IoPort.FALLING,callback=wow1,bouncetime=200)
