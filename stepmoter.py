import RPi.GPIO as IoPort
import time

def step1(gpio,delay):
    IoPort.output(gpio[0], False)
    IoPort.output(gpio[1], True)
    IoPort.output(gpio[2], True)
    IoPort.output(gpio[3], True)
    time.sleep(delay)

def step2(gpio,delay):
    IoPort.output(gpio[0], False)
    IoPort.output(gpio[1], True)
    IoPort.output(gpio[2], False)
    IoPort.output(gpio[3], True)
    time.sleep(delay)
    
def step3(gpio,delay):
    IoPort.output(gpio[0], True)
    IoPort.output(gpio[1], True)
    IoPort.output(gpio[2], False)
    IoPort.output(gpio[3], True)
    time.sleep(delay)

def step4(gpio,delay):
    IoPort.output(gpio[0], True)
    IoPort.output(gpio[1], False)
    IoPort.output(gpio[2], False)
    IoPort.output(gpio[3], True)
    time.sleep(delay)

def step5(gpio,delay):
    IoPort.output(gpio[0], True)
    IoPort.output(gpio[1], False)
    IoPort.output(gpio[2], True)
    IoPort.output(gpio[3], True)
    time.sleep(delay)

def step6(gpio,delay):
    IoPort.output(gpio[0], True)
    IoPort.output(gpio[1], False)
    IoPort.output(gpio[2], True)
    IoPort.output(gpio[3], False)
    time.sleep(delay)

def step7(gpio,delay):
    IoPort.output(gpio[0], True)
    IoPort.output(gpio[1], True)
    IoPort.output(gpio[2], True)
    IoPort.output(gpio[3], False)
    time.sleep(delay)

def step8(gpio,delay):
    IoPort.output(gpio[0], False)
    IoPort.output(gpio[1], True)
    IoPort.output(gpio[2], True)
    IoPort.output(gpio[3], False)
    time.sleep(delay)
    
gpio =[6,19,5,13]
delay = 0.0008

IoPort.setmode(IoPort.BCM)
IoPort.setup(gpio, IoPort.OUT)
IoPort.output(gpio, True)

while True:
    step1(gpio,delay)
    step2(gpio,delay)
    step3(gpio,delay)
    step4(gpio,delay)
    step5(gpio,delay)
    step6(gpio,delay)
    step7(gpio,delay)
    step8(gpio,delay)    

    
