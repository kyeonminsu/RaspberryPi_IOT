from midterm import kyeonminsu201510045class
import RPi.GPIO as IoPort

print("Start!!")
#socket
clsSock=kyeonminsu201510045class.midterm()
#buzzer
clsBuzzer=kyeonminsu201510045class.Buzzer()
#Led
clsLed=kyeonminsu201510045class.Led()

clsSock.server_socket('192.168.0.8',6756)
print("Client -> Server Connected!!")
for i in range(0,3):
    clsLed.Led3On()

while True:
    recv_data=clsSock.Receive()
    if(recv_data=='go'):
        print("Ok!! Music Start!!")
    if(recv_data=='10'):
        for j in range(0,2):
            clsLed.Led3On()
    if(recv_data=='q'):
        break
    clsBuzzer.BuzzerOn(recv_data)
    clsLed.BuzzerLedOn(recv_data)
    
    
print("END")
