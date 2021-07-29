import RPi.GPIO as IoPort
import time

IoPort.setmode(IoPort.BCM)
IoPort.setup(22, IoPort.OUT)

IoPort.setup(4, IoPort.IN)
IoPort.setup(23, IoPort.IN)


def On(x):
    print("On")
    if(IoPort.input(x)==False):
        IoPort.output(22, True)
    
    
def Off(x):
    print("Off")
    if(IoPort.input(x)==False):
        IoPort.output(22, False)

    
IoPort.add_event_detect(4,IoPort.FALLING,callback=On,bouncetime=200)
IoPort.add_event_detect(23,IoPort.FALLING,callback=Off,bouncetime=200)
i=0
while(i<500):
    print("Start")
    time.sleep(5)
    i=i+1




