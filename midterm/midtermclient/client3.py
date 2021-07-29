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
clsFile=kyeonminsu201510045class.file_str()
#Led
clsLed=kyeonminsu201510045class.Led()

clsSock.client_socket('192.168.0.2',5566)
print("Client -> Server Connected!!")
clsFile.file_write()

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
    if(i==1):
        send_data=clsFile.file_read()
        clsSock.Send(send_data)
        if(send_data==''):
            send_data='Q'
            clsSock.Send(send_data)
            clsFile.file_close()
            break
        recv_data=clsSock.Receive()
        print(recv_data)
    
print("END")
