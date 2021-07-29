import RPi.GPIO as IoPort
import time

def Speedup(x):
    global i
    i=1
def Speeddown(x):    
    global i
    i=2

Enable = 26
Right = 19
Left = 13
key1 = 17

IoPort.setmode(IoPort.BCM)
IoPort.setup(Enable, IoPort.OUT)
IoPort.setup(Right, IoPort.OUT)
IoPort.setup(Left, IoPort.OUT)

IoPort.output(Enable, True)
IoPort.output(Left, False)
p=IoPort.PWM(Right, 1000)

p.start(0)
time.sleep(1)
ulist=[10,20,30,40,50,60,70,80,90,100]
dlist=[100,90,80,70,60,50,40,30,20,10]

IoPort.add_event_detect(key1,IoPort.FALLING,callback=Speedup,bouncetime=200)
IoPort.add_event_detect(key1,IoPort.RISING,callback=Speeddown,bouncetime=200)

i=0
while True:
    if(i==1):
        for sp in ulist:
            p.ChangeDutyCycle(sp)
            time.sleep(1)
        time.sleep(2)
        i=0

    if(i==2):
        for sp in dlist:
            p.ChangeDutyCycle(sp)
            time.sleep(0.01)
        i=0     
    IoPort.output(Enable, False)
