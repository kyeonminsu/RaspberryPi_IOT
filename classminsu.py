import RPi.GPIO as IoPort
#IoPort.setup(arr,IoPort.OUT)
#IoPort.setup(25,IoPort.IN)
#IoPort.setmode(IoPort.BCM)
IoPort.setmode(IoPort.BCM)
#IoPort.setup(arr,IoPort.OUT)
IoPort.setup(17,IoPort.OUT)
IoPort.setup(27,IoPort.OUT)
IoPort.setup(22,IoPort.OUT)
IoPort.setup(26,IoPort.OUT)
IoPort.setup(19,IoPort.OUT)
IoPort.setup(13,IoPort.OUT)
IoPort.setup(1,IoPort.OUT)
IoPort.setup(12,IoPort.OUT)
IoPort.setup(4,IoPort.OUT)
IoPort.setup(18,IoPort.OUT)
IoPort.setup(23,IoPort.OUT)
IoPort.setup(24,IoPort.OUT)
IoPort.setup(25, IoPort.IN) #start 25
IoPort.setup(6, IoPort.IN) #stop 6
IoPort.setup(5, IoPort.IN) #reSet
#IoPort.setup(0, IoPort.IN) #LED


class seg:
    def __init__(self):
        IoPort.setmode(IoPort.BCM)
        #IoPort.setup(arr,IoPort.OUT)
        IoPort.setup(17,IoPort.OUT)
        IoPort.setup(27,IoPort.OUT)
        IoPort.setup(22,IoPort.OUT)
        IoPort.setup(26,IoPort.OUT)
        IoPort.setup(19,IoPort.OUT)
        IoPort.setup(13,IoPort.OUT)
        IoPort.setup(1,IoPort.OUT)
        IoPort.setup(12,IoPort.OUT)
        IoPort.setup(4,IoPort.OUT)
        IoPort.setup(18,IoPort.OUT)
        IoPort.setup(23,IoPort.OUT)
        IoPort.setup(24,IoPort.OUT)
        IoPort.setup(25, IoPort.IN) #start 25
        IoPort.setup(6, IoPort.IN) #stop 6
        IoPort.setup(5, IoPort.IN) #reSet
        #IoPort.setup(0, IoPort.IN) #LED
    def seg_0():
        IoPort.output(17,False)
        IoPort.output(27,False)
        IoPort.output(22,False)
        IoPort.output(26,False)
        IoPort.output(19,False)
        IoPort.output(13,False)
        IoPort.output(1,True)
    def seg_1():
        IoPort.output(17,True)
        IoPort.output(27,False)
        IoPort.output(22,False)
        IoPort.output(26,True)    
        IoPort.output(19,True)
        IoPort.output(13,True)
        IoPort.output(1,True)
    def seg_2():
        IoPort.output(17,False)
        IoPort.output(27,False)
        IoPort.output(22,True)
        IoPort.output(26,False)
        IoPort.output(19,False)
        IoPort.output(13,True)
        IoPort.output(1,False)
    def seg_3():
        IoPort.output(17,False)
        IoPort.output(27,False)
        IoPort.output(22,False)
        IoPort.output(26,False)
        IoPort.output(19,True)
        IoPort.output(13,True)
        IoPort.output(1,False)  
    def seg_4():
        IoPort.output(17,True)
        IoPort.output(27,False)
        IoPort.output(22,False)
        IoPort.output(26,True)
        IoPort.output(19,True)
        IoPort.output(13,False)
        IoPort.output(1,False)
    def seg_5():
        IoPort.output(17,False)
        IoPort.output(27,True)
        IoPort.output(22,False)
        IoPort.output(26,False)
        IoPort.output(19,True)
        IoPort.output(13,False)
        IoPort.output(1,False)
    def seg_6():
        IoPort.output(17,False)
        IoPort.output(27,True)
        IoPort.output(22,False)
        IoPort.output(26,False)
        IoPort.output(19,False)
        IoPort.output(13,False)
        IoPort.output(1,False)
    def seg_7():
        IoPort.output(17,False)
        IoPort.output(27,False)
        IoPort.output(22,False)
        IoPort.output(26,True)
        IoPort.output(19,True)
        IoPort.output(13,True)
        IoPort.output(1,True)
    def seg_8():
        IoPort.output(17,False)
        IoPort.output(27,False)
        IoPort.output(22,False)
        IoPort.output(26,False)
        IoPort.output(19,False)
        IoPort.output(13,False)
        IoPort.output(1,False)
    def seg_9():
        IoPort.output(17,False)
        IoPort.output(27,False)
        IoPort.output(22,False)
        IoPort.output(26,True)
        IoPort.output(19,True)
        IoPort.output(13,False)
        IoPort.output(1,False)

    def seg_C(num):
        if (num==0):
            IoPort.output(4,True)
            IoPort.output(18,False)
            IoPort.output(23,False)
            IoPort.output(24,False)
            IoPort.output(12,True)
        elif(num==1):
            IoPort.output(4,False)
            IoPort.output(18,True)
            IoPort.output(23,False)
            IoPort.output(24,False)
            IoPort.output(12,False)
        elif(num==2):
            IoPort.output(4,False)
            IoPort.output(18,False)
            IoPort.output(23,True)
            IoPort.output(24,False)
            IoPort.output(12,True)
        elif(num==3):
            IoPort.output(4,False)
            IoPort.output(18,False)
            IoPort.output(23,False)
            IoPort.output(24,True)
            IoPort.output(12,True)


    






    

       
