import RPi.GPIO as minsu
import time
minsu.setmode(minsu.BCM)
minsu.setup(18,minsu.OUT)
minsu.setup(17,minsu.OUT)
minsu.setup(27,minsu.OUT)
minsu.setup(22,minsu.OUT)

cubes=[18,17,27,22]

def LED_ON(Port, Delay):
    num=Port
    if(num==0):
         for i in range(0,4):
             minsu.output(cubes[i], True)
    elif(num==1):
        print(0)
        minsu.output(18, True)
        time.sleep(1)
        minsu.output(18, False)
    elif(num==2):
        minsu.output(cubes[1], True)
    elif(num==3):
        minsu.output(cubes[2], True)
    elif(num==4):
        minsu.output(cubes[3], True)
    else:
        print("No port!!")
    time.sleep(Delay)    

def LED_ON(Port, Delay):
    if(Port==0):
         for i in range(0,4):
             minsu.output(cubes[i], False)
    elif(Port==1):
        minsu.output(cubes[0], False)
    elif(Port==2):
        minsu.output(cubes[1], False)
    elif(Port==3):
        minsu.output(cubes[2], False)
    elif(Port==4):
        minsu.output(cubes[3], False)
    else:
        print("No port!!")
    time.sleep(Delay)

    

Delay=0
Port=0
num=0
print("Start!")
while(True):
    Port=eval(input("Select LED number(0:All)"))
    num=int(input("1:ON, 2:OFF, 3:Blink, 4:END"))

    Delay=1
    if(num==1):
        print(0)
        LED_ON(Port, Delay)
    elif(num==2):
        LED_OFF(Port, Delay)
    elif(num==3):
        print("zas")
    else:
        print("END")
        break












        
