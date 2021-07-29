import RPi.GPIO as minsu
import time
sw=4
minsu.setmode(minsu.BCM)
minsu.setup(22, minsu.OUT)
minsu.setup(21, minsu.OUT)
minsu.setup(16, minsu.OUT)
minsu.setup(12, minsu.OUT)
minsu.setup(sw, minsu.IN)

arr=[21,16,22]
def wow():
    i=0;
    while(i<4):
        minsu.output(arr[i], True)
        time.sleep(0.7)
        minsu.output(arr[i], False)
        time.sleep(0.7)
        i=i+1

def wow1():
    i=3;
    while(i>0):
        minsu.output(arr[i], True)
        time.sleep(0.7)
        minsu.output(arr[i], False)
        time.sleep(0.7)
        i=i-1


print("Start!!")
while(True):
    rcv=minsu.input(sw)
    if(rcv==0):
        i=0;
        while(i<4):
            minsu.output(arr[i], True)
            time.sleep(0.7)
            minsu.output(arr[i], False)
            time.sleep(0.7)
            i=i+1
    else:
        i=3;
        while(i>0):
            minsu.output(arr[i], True)
            time.sleep(0.7)
            minsu.output(arr[i], False)
            time.sleep(0.7)
            i=i-1



