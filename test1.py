import RPi.GPIO as minsu
import time
import random
minsu.setmode(minsu.BCM)
minsu.setup(18,minsu.OUT) 
minsu.setup(17,minsu.OUT) 
minsu.setup(27,minsu.OUT)
minsu.setup(22,minsu.OUT)

def Wow(i):
    cubes=[18, 17, 27, 22]    
    while(True):
        minsu.output(cubes[i], True)
        time.sleep(1)
        minsu.output(cubes[i], False)
        if(i==0):
            break
        minsu.output(cubes[i-1], True)
        time.sleep(1)
        minsu.output(cubes[i-1], False)
        if(i==1):
            break
        minsu.output(cubes[i-2], True)
        time.sleep(1)
        minsu.output(cubes[i-2], False)
        if(i==2):
            break
       
        
    
#num=int(input("Select !!(0=Right, 1=Left) else End"))
for i in range (0,4):
    Wow(i)
    
