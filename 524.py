import RPi.GPIO as IoPort
import time
sw=4
IoPort.setmode(IoPort.BCM)
IoPort.setup(22, IoPort.OUT)
IoPort.setup(17, IoPort.OUT)
IoPort.setup(27, IoPort.OUT)
IoPort.setup(18, IoPort.OUT)
IoPort.setup(sw, IoPort.IN)
arr=[22,17,27,18]

while True:
    rcv=IoPort.input(sw)
    time.sleep(0.1)
    for i in range (0, 4):
        if(rcv==0):
            IoPort.output(arr[i], True)
            time.sleep(0.5)
            IoPort.output(arr[i], False)
            time.sleep(0.5)
        elif(rcv==1):
            for i in range (0, 4):
                IoPort.output(arr[i], False)


    #if(rcv==0):
     #   time.sleep(0.1)
    #elif(rcv==1):
     #   time.sleep(0.1)
      #  for i in range (0, 4):
       #     IoPort.output(arr[i], False)
