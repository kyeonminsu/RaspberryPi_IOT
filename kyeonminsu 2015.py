import classminsu
import time
import RPi.GPIO as IoPort

cls=classminsu.seg
arr=[0,0,0,0,0]
arr1=[0]

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

def stopwatch(second): #reset
    global cotime
    cotime=0.001

def startwatch(second):
    global cotime
    if(arr[0]==0):
        cotime=0.0005
        arr[0]=1
    elif(arr[0]==1):
        cotime=0.00025
        arr[0]=arr[0]+1
    elif(arr[0]==2):
        cotime=0.000001
        
def reset(second):
    global m
    global cotime
    cotime=0.001
    m=0
    i=0
    for i in range(0,4):
        arr[i]=0
"""
def seg_ON():
    j=0
    cotime=0.001
    for j in range(0, 4):
        cls.seg_C(j)
        count(arr[j])
        time.sleep(cotime)

def LED_ON():
     global Led
     Led=1
     IoPort.output(0,True)
     time.sleep(0.5)
def LED_OFF():
     global Led
     Led=0
     IoPort.output(0,False)
     time.sleep(0.5)
"""
     
IoPort.add_event_detect(25,IoPort.FALLING,callback=startwatch,bouncetime=200) #start
IoPort.add_event_detect(6,IoPort.FALLING,callback=stopwatch,bouncetime=200) #stop
IoPort.add_event_detect(5,IoPort.FALLING,callback=reset,bouncetime=200) #reSet
i=0
j=0
t=0
sum1=0
sum2=0
sum3=0
cotime=0.001
k=0 #stop variable
h=0 #stop variable
m=0
s=0 #stat variable
r=0 #reset
Led=0
print("Start")
while(True):
    if(m%3==0):
        sum1=m
        
    if(sum1<10):
        arr[0]=sum1
    elif(sum1>10 and sum1<100):
        arr[0]=sum1%10
        arr[1]=sum1//10
    elif(sum1>100 and sum1<1000):
        arr[2]=sum1//100
        sum1=sum1%100
        arr[0]=sum1%10
        arr[1]=sum1//10
    elif(sum1>1000):
         arr[3]=sum1//1000
         sum3=sum1%1000
         arr[2]=sum3//100
         sum2=sum3%100
         arr[1]=sum2//10
         sum1=sum2%10
         arr[0]=sum1

    m=m+1    
    while(True):
        for j in range(0, 4):
            for j in range(0, 4):
                cls.seg_C(j)
                count(arr[j])
                time.sleep(cotime)
               #LED_ON()
                """
                if(Led==1):
                    LED_OFF()
                """
                      
            t=t+1
            if(k==1):
                while(True):
                    if(s==1):
                        s=0
                        k=0
                        break
                    for j in range(0, 4):
                        cls.seg_C(j)
                        count(arr[j])
                        time.sleep(cotime)
            if(t==100):
                break
        if(t==100):
            t=0
            break
