import RPi.GPIO as IoPort
import classminsu
import time
#sw=25
#4=c0
#18=c1
#23=c2
#24=c3
#arr=[17,27,22,26,19,13,1,12]

def ON(num):
    global i
    if(IoPort.input(25)==False):
        i=-1
    else:
        i=-1
        

print("Start!")
i=0
cls=classminsu.seg

IoPort.add_event_detect(25,IoPort.FALLING,callback=ON,bouncetime=200)
while(1):
    if(i==10):
        i=0
    cls.segON(i)
    #classminsu.seg.segON(i)
    time.sleep(1)
    i=i+1
    
    
