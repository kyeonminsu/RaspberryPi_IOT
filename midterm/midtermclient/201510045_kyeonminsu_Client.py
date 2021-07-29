from midterm import kyeonminsu201510045class
import RPi.GPIO as IoPort
import time


def DataSend(x):
    global i
    send_data='0'
    clsSock.Sendmusic(send_data)
    i=1

def ReSet(x):
    clsSock.reset()
    print("Initialized")

sw1=4
sw2=12
IoPort.setmode(IoPort.BCM)
IoPort.setup(sw1, IoPort.IN)

IoPort.setup(sw2, IoPort.IN)
print("Start!!")
#socket
clsSock=kyeonminsu201510045class.midterm()

clsSock.client_socket('192.168.0.8',6756)
print("Client -> Server Connected!!")

IoPort.add_event_detect(sw1,IoPort.FALLING,callback=DataSend,bouncetime=200)
IoPort.add_event_detect(sw2,IoPort.FALLING,callback=ReSet,bouncetime=200)
i=0
while True:
    if(i==1):
        send_data = input("message : ")
        clsSock.Send(send_data)
        if(send_data=='q'):
            break
        i=0
 

print("END")
