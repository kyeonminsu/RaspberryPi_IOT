import socket
import RPi.GPIO as IoPort
import time
IoPort.setmode(IoPort.BCM)
#TCP
class midterm:
    def __init__(self):
        self.com_socket=socket.socket()
        self.connection=self.com_socket
        self.arr=['1','2','3','4','5','6','7','8']        
        self.i=0
    #server function
    def server_socket(self,IP,Port):
        self.com_socket.bind((IP,Port))
        self.com_socket.listen(10)
        self.connection,self.address = self.com_socket.accept()
    #client function
    def client_socket(self,IP,Port):
        self.com_socket.connect((IP,Port))

    #data send/recv
    def Sendmusic(self, data):
        if(data=='0'):
            self.connection.send(bytes(self.arr[self.i],"UTF-8"))
            if(self.i==0):
                print("DO")
            elif(self.i==1):
                print("Re")
            elif(self.i==2):
                print("Me")
            elif(self.i==3):
                print("Fa")
            elif(self.i==4):
                print("Sol")
            elif(self.i==5):
                print("Ra")
            elif(self.i==6):
                print("Si")
            elif(self.i==7):
                print("High_DO")
            self.i=self.i+1
            if(self.i==8):
                self.i=0
    def reset(self):
        self.i=0
        data='10'
        self.connection.send(bytes(data,"UTF-8"))
    
    def Send(self, data):
        self.connection.send(bytes(data,"UTF-8"))
        
    def Receive(self):
        return self.connection.recv(4096).decode("UTF-8")

    def SendByte(self, data):
        self.connection.send(bytes(data))
        
    def ReceiveByte(self):
        return self.connection.recv(1024)

    def SendBinary(self, data):
        self.connection.send(data)

    def ReceiveBinary(self):
        return self.connection.recv(4096)


class Buzzer:
    def __init__(self):
        self.buzzer=17
        IoPort.setup(self.buzzer,IoPort.OUT)
        

    def BuzzerOn(self, data):
        #Do
        if(data=='1'):
            for a in range(0, 20):
                IoPort.output(self.buzzer, True)
                time.sleep(0.0076452599388379195)
                IoPort.output(self.buzzer, False)
                time.sleep(0.0076452599388379195)
        #Re
        elif(data=='2'):
            for a in range(0, 20):
                IoPort.output(self.buzzer, True)
                time.sleep(0.006811989100817438)
                IoPort.output(self.buzzer, False)
                time.sleep(0.006811989100817438)
        #Mi
        elif(data=='3'):
            for a in range(0, 20):
                IoPort.output(self.buzzer, True)
                time.sleep(0.006067961165048544)
                IoPort.output(self.buzzer, False)
                time.sleep(0.006067961165048544)
        #Fa
        elif(data=='4'):
            for a in range(0, 20):
                IoPort.output(self.buzzer, True)
                time.sleep(0.00572737686139748)
                IoPort.output(self.buzzer, False)
                time.sleep(0.00572737686139748)
        #Sol
        elif(data=='5'):
            for a in range(0, 20):
                IoPort.output(self.buzzer, True)
                time.sleep(0.00510204081632653)
                IoPort.output(self.buzzer, False)
                time.sleep(0.00510204081632653)
        #Ra
        elif(data=='6'):
            for a in range(0, 30):
                IoPort.output(self.buzzer, True)
                time.sleep(0.004545454545454545)
                IoPort.output(self.buzzer, False)
                time.sleep(0.004545454545454545)
        #Si
        elif(data=='7'):
            for a in range(0, 35):
                IoPort.output(self.buzzer, True)
                time.sleep(0.004050222762251924)
                IoPort.output(self.buzzer, False)
                time.sleep(0.004050222762251924)
        #high_do
        elif(data=='8'):
            for a in range(0, 40):
                IoPort.output(self.buzzer, True)
                time.sleep(0.0038314176245210726)
                IoPort.output(self.buzzer, False)
                time.sleep(0.0038314176245210726)

        
    

class Led:
    def __init__(self):
        self.led1=27
        self.led2=22 
        self.led3=5 
        self.led4=6
        self.led5=13
        self.led6=26
        self.led7=23
        self.led8=24
        
        IoPort.setup(self.led1, IoPort.OUT)
        IoPort.setup(self.led2, IoPort.OUT)
        IoPort.setup(self.led3, IoPort.OUT)
        IoPort.setup(self.led4, IoPort.OUT)
        IoPort.setup(self.led5, IoPort.OUT)
        IoPort.setup(self.led6, IoPort.OUT)
        IoPort.setup(self.led7, IoPort.OUT)
        IoPort.setup(self.led8, IoPort.OUT)
        
    def Led3On(self):
        IoPort.output(self.led1, True)
        IoPort.output(self.led2, True)
        IoPort.output(self.led3, True)
        IoPort.output(self.led4, True)
        IoPort.output(self.led5, True)
        IoPort.output(self.led6, True)
        IoPort.output(self.led7, True)
        IoPort.output(self.led8, True)
        time.sleep(1)
        IoPort.output(self.led1, False)
        IoPort.output(self.led2, False)
        IoPort.output(self.led3, False)
        IoPort.output(self.led4, False)
        IoPort.output(self.led5, False)
        IoPort.output(self.led6, False)
        IoPort.output(self.led7, False)
        IoPort.output(self.led8, False)
        time.sleep(1)

    def BuzzerLedOn(self, data):
         #Do
        if(data=='1'):
            print("Do")
            IoPort.output(self.led1, True)
            time.sleep(0.5)
            IoPort.output(self.led1, False)
            time.sleep(0.5)
        #Re
        elif(data=='2'):
            print("Re")
            IoPort.output(self.led2, True)
            time.sleep(0.5)
            IoPort.output(self.led2, False)
            time.sleep(0.5)
        #Mi
        elif(data=='3'):
            print("Mi")
            IoPort.output(self.led3, True)
            time.sleep(0.5)
            IoPort.output(self.led3, False)
            time.sleep(0.5)
        #Fa
        elif(data=='4'):
            print("Fa")
            IoPort.output(self.led4, True)
            time.sleep(0.5)
            IoPort.output(self.led4, False)
            time.sleep(0.5)
        #Sol
        elif(data=='5'):
            print("Sol")
            IoPort.output(self.led5, True)
            time.sleep(0.5)
            IoPort.output(self.led5, False)
            time.sleep(0.5)
        #Ra
        elif(data=='6'):
            print("Ra")
            IoPort.output(self.led6, True)
            time.sleep(0.5)
            IoPort.output(self.led6, False)
            time.sleep(0.5)
        #Si
        elif(data=='7'):
            print("Si")
            IoPort.output(self.led7, True)
            time.sleep(0.5)
            IoPort.output(self.led7, False)
            time.sleep(0.5)
        #high_do
        elif(data=='8'):
            print("high_Do")
            IoPort.output(self.led8, True)
            time.sleep(0.5)
            IoPort.output(self.led8, False)
            time.sleep(0.5)
    
   

        
