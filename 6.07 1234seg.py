import classminsu
import time
import RPi.GPIO as IoPort
cls=classminsu.seg

def C0(i):
    while(i<10):
        #c0
        global j
        IoPort.output(24,True) 
        cls.segON(i)
        time.sleep(1)
        IoPort.output(24,False)
        i=i+1
        time.sleep(0.01)
        if(i==9):
             j=i+1

                

print("Start!")
j=0
while(1):
    C0(j)
    time.sleep(0.01)
    
    
    
