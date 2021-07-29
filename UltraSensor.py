import RPi.GPIO as gpio
import time


def Echofunc1(echo1):
    while gpio.input(echo1)==0:
        pulse_start=time.clock()
    return pulse_start 

def Echofunc2(echo2):
    while gpio.input(echo2)==1:
        pulse_end=time.clock()
    return pulse_end

def BuzzerOn(buzzer):
    gpio.output(buzzer, True)
    time.sleep(1/196)
    gpio.output(buzzer, False)
    time.sleep(1/196)
            
echo=4
trig=17
buzzer=27
gpio.setmode(gpio.BCM)
gpio.setup(trig, gpio.OUT)
gpio.setup(echo, gpio.IN)
gpio.setup(buzzer, gpio.OUT)

print("Start!!")

while True:
    gpio.output(trig, False)
    time.sleep(0.01)
    gpio.output(trig, True)
    time.sleep(0.00001)
    gpio.output(trig, False)

    pulse_start=Echofunc1(echo)
    pulse_end=Echofunc2(echo)

    pulse_duration = pulse_end- pulse_start
    distance =  pulse_duration*17421
    distance =  round(distance, 2)

    if (distance>0 and distance<10):
        print("Distance : ", distance, "cm") 
        BuzzerOn(buzzer)
        time.sleep(int(distance*0.01))
    elif(distance>10 and distance<21):
        print("Distance : ", distance, "cm") 
        BuzzerOn(buzzer)
        time.sleep(int(distance*0.03))
           
        
 
