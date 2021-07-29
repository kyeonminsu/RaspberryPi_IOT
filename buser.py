import RPi.GPIO as IoPort
import time

IoPort.setmode(IoPort.BCM)
IoPort.setup(18, IoPort.OUT)

arr=[0.0032,0.0036,0.0040,0.0036,0.0032,0.0032,0.0032]
while True:
    for a in range(0, 1000):
        IoPort.output(18, True)
        time.sleep(arr[a])
        IoPort.output(18, False)
        time.sleep(arr[a])


    
 
