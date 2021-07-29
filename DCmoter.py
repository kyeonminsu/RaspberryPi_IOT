import RPi.GPIO as IoPort

key1 = 17
key2 = 27
Enable = 26
Right = 19
Left = 13

IoPort.setmode(IoPort.BCM)
IoPort.setup(key1, IoPort.IN)
IoPort.setup(key2, IoPort.IN)
IoPort.setup(Enable, IoPort.OUT)
IoPort.setup(Right, IoPort.OUT)
IoPort.setup(Left, IoPort.OUT)

try:
    while True:
        while IoPort.input(key1)==False:
            IoPort.output(Left, False)
            IoPort.output(Right, True)
            IoPort.output(Enable, True)
        while IoPort.input(key2)==False:
            IoPort.output(Left, False)
            IoPort.output(Right, True)
            IoPort.output(Enable, False)
        IoPort.output(Enable, False)
except:
    IoPort.output(Enable, False )
