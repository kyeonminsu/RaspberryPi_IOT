import classminsu
import time
import RPi.GPIO as IoPort

cls=classminsu.seg
arr=[0,0,0,0,0]

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

i=0
j=0
t=0
print("Start")
while(True):
    arr[0]=arr[0]+1
    for i in range(0, 4):
        if(arr[i]==10):
            arr[i]=0
            if(i<=3):
                arr[i+1]=arr[i+1]+1
            else:
                for j in range(0,4):
                    arr[j]=0
    while(True):
        for j in range(0, 4):
            cls.seg_C(j)
            count(arr[j])
            time.sleep(0.001)
            t=t+1
            if(t==100) :
                break
        if(t==100):
            t=0
            break        

            
            
        

    

   
