from midterm import kyeonminsu201510045class
import RPi.GPIO as IoPort
import time

def buzzerdata(x):
    send_data='1'
    clsSock.Send(send_data)
    
sw=4
IoPort.setmode(IoPort.BCM)
IoPort.setup(sw, IoPort.IN)
print("Start!!")
#socket
clsSock=kyeonminsu201510045class.midterm()
#file
#clsFile=kyeonminsu201510045class.file_str()
#Led
clsLed=kyeonminsu201510045class.Led()
clsSock.client_socket('192.168.0.2',5556)
print("Client -> Server Connected!!")
#clsFile.file_write()

i=0
IoPort.add_event_detect(sw,IoPort.FALLING,callback=buzzerdata,bouncetime=200)
while True:
    if(i==0):
        led=clsSock.Receive()
    if(led=='2'):
        clsLed.LedOn()
        print("Led On")
        led=2
        i=1
        continue
    if(i==1):
        recv_data=clsSock.Receive()
        print(recv_data)
        send_data = input("message : ")
        clsSock.Send(send_data)
        if(send_data=='Q'):
            break
        
print("END")
