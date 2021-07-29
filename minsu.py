import RPi.GPIO as minsu
import time
minsu.setmode(minsu.BCM)
minsu.setup(18,minsu.OUT) 
minsu.setup(17,minsu.OUT) 
minsu.setup(27,minsu.OUT)
minsu.setup(22,minsu.OUT)

def Wow():
    cubes=[18, 17, 27, 22]
    i=0
    while(i<4):
            minsu.output(cubes[i], True)
            time.sleep(1)
            minsu.output(cubes[i], False)
            time.sleep(1)
            i=i+1        
   
def Wow1():

    cubes1=[18, 17, 27, 22] 
    i=3
    while(i>=0):
        minsu.output(cubes1[i], True)
        time.sleep(1)
        minsu.output(cubes1[i], False)
        time.sleep(1)
        i=i-1
        
num=int(input("Select !!(0=Right, 1=Left)"))

if(num==0):
    Wow()
if(num==1):
    Wow1()

