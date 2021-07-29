import RPi.GPIO as IoPort
import time

IoPort.setmode(IoPort.BCM)
IoPort.setup(18, IoPort.OUT)
p=IoPort.PWM(18, 1000)
p.start(0)

while True:
    IoPort.output(18, True)
    time.sleep(0.0000001)
    IoPort.output(18, False)
    time.sleep(0.0000001)
