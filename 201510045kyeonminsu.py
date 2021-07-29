import classminsu
import time
import RPi.GPIO as IoPort

cls=classminsu.seg
arr=[0,0,0,0,0]
#temp=[0,0,0,0,0]

def count(num):
    if(num==0):
        classminsu.seg.seg_0()
    elif(num==1):
        classminsu.seg.seg_1()
    elif(num==2):
        classminsu.seg.seg_2()
    elif(num==3):
        classminsu.seg.seg_3() 
    elif(num==4):
        classminsu.seg.seg_4()
    elif(num==5):
        classminsu.seg.seg_5()
    elif(num==6):
        classminsu.seg.seg_6()
    elif(num==7):
        classminsu.seg.seg_7()
    elif(num==8):
        classminsu.seg.seg_8()
    elif(num==9):
        classminsu.seg.seg_9()

def stopwatch(second):
    global k
    k=1

def startwatch(second):
    global s
    s=1

def reset(second):
    i=0
    for i in range(0,4):
        arr[i]=0
        
def seg_ON():
    j=0
    for j in range(0, 4):
        cls.seg_C(j)
        count(arr[j])
        time.sleep(0.001)
   
IoPort.add_event_detect(25,IoPort.FALLING,callback=startwatch,bouncetime=200) #start
IoPort.add_event_detect(6,IoPort.FALLING,callback=stopwatch,bouncetime=200) #stop
IoPort.add_event_detect(5,IoPort.FALLING,callback=reset,bouncetime=200) #reSet
i=0
j=0
t=0

k=0 #stop variable
h=0 #stop variable

s=0 #stat variable
print("Start")
while(True):
    arr[0]=arr[0]+3
    for i in range(0, 4):
        if(arr[i]==10):
            arr[i]=0
            if(i<=3):
                arr[i+1]=arr[i+1]+3
            else:
                reset(i)
    while(True):
        for j in range(0, 4):
            seg_ON()
            t=t+1
            if(k==1):
                while(True):
                    if(s==1):
                        s=0
                        k=0
                        break
                    seg_ON()
            if(t==100):
                break
        if(t==100):
            t=0
            break







































        
