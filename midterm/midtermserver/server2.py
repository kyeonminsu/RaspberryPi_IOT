#import kyeonminsu201510045class
from midterm import kyeonminsu201510045class
import RPi.GPIO as IoPort

print("Start!!")
#socket
clsSock=kyeonminsu201510045class.midterm()
#buzzer
clsBuzzer=kyeonminsu201510045class.Buzzer()
#file
#clsFile=kyeonminsu201510045class.file_str()

clsSock.server_socket('192.168.0.2',5556)
print("Client -> Server Connected!!")
#clsFile.file_read()

led=0
while True:
    recv_data=clsSock.Receive()
    print(recv_data)
    if(recv_data=='Q'):
        break
    if(recv_data=='1'):
        clsBuzzer.BuzzerOn()
        led=1
    if(led==1):
        led_data='2'
        clsSock.Send(led_data)
        led=0
    send_data = input("message : ")
    clsSock.Send(send_data)
        
print("END")
