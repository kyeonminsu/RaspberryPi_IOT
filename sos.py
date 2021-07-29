import RPi.GPIO as minsu
import time
minsu.setmode(minsu.BCM)
minsu.setup(18,minsu.OUT) 
minsu.setup(17,minsu.OUT)
minsu.setup(27,minsu.OUT) 
minsu.setup(22,minsu.OUT)

cubes=[18,17,27,22]

A=0
array=[]
i=0
B=0
num=int(input("number input\n"))
while(True):
    A=num//2
    B=num%2
    array.append(B)
    num=A
    i=i+1
    if(num==1):
        array.append(num)
        break
    
print("Left to right =>1,2,4,8.........")
print(array)
i=i+1
j=0
while(j<i+1):
    if(array[j]==0):
        minsu.output(cubes[j],False)
    else:
        minsu.output(cubes[j],True)
    time.sleep(1)
    minsu.output(cubes[j],False)
    j=j+1
         
