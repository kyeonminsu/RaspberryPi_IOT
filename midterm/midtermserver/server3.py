#import kyeonminsu201510045class
from midterm import kyeonminsu201510045class
import RPi.GPIO as IoPort

print("Start!!")
#socket
clsSock=kyeonminsu201510045class.midterm()
#buzzer
clsBuzzer=kyeonminsu201510045class.Buzzer()
#file
clsFile=kyeonminsu201510045class.file_str()

clsSock.server_socket('192.168.0.2',5566)
print("Client -> Server Connected!!")

j=0
led=0
while True:
    if(j==0):
        recv_data=clsSock.Receive()
        print(recv_data)
        
    if(recv_data=='1'):
        clsBuzzer.BuzzerOn()
        led=1
    if(led==1):
        led_data='2'
        clsSock.Send(led_data)
        led=2
        j=1
        
    if(led==2):
        recv_data=clsSock.Receive()
        clsFile.file_write2(recv_data)
    
        if(recv_data=='Q'):
            clsFile.file_close()
            break
    send_data = 'read good'
    clsSock.Send(send_data)
        
print("END")
