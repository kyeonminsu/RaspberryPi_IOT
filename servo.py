import RPi.GPIO as IoPort
import time


def Left(x):
    print("Left")
    IoPort.output(servo, True)
    time.sleep(0.0018)
    IoPort.output(servo, False)
    time.sleep(0.002)
    
def Right(x):
    print("Right")
    IoPort.output(servo, True)
    time.sleep(0.008)
    IoPort.output(servo, False)
    time.sleep(0.02)
    
servo=26
key1 = 17
key2 = 27

IoPort.setmode(IoPort.BCM)
IoPort.setup(servo, IoPort.OUT)
IoPort.setup(key1, IoPort.IN)
IoPort.setup(key2, IoPort.IN)

IoPort.add_event_detect(key1,IoPort.FALLING,callback=Left,bouncetime=200)
IoPort.add_event_detect(key2,IoPort.FALLING,callback=Right,bouncetime=200)


while True:
    time.sleep(0.01)
