import RPi.GPIO as IoPort
import time
import socket


def music(buzzer):
    for a in range(0, 500):
        IoPort.output(18, True)
        time.sleep(buzzer)
        IoPort.output(18, False)
        time.sleep(buzzer)
        



IoPort.setmode(IoPort.BCM)
IoPort.setup(18, IoPort.OUT)
p=IoPort.PWM(18, 1000)
p.start(0)
print("start!!")
com_socket=socket.socket()
com_socket.bind(('192.168.0.7',3133))
com_socket.listen(10)
connection, address = com_socket.accept()
print(address, "Connected good")

while True:
    buzzer=connection.recv(4096).decode("UTF-8")
    print(buzzer)
    if(buzzer=='1'):
        buzzer1=0.0038
        music(buzzer1)
    elif(buzzer=='2'):
        buzzer1=0.0034
        music(buzzer1)
    elif(buzzer=='3'):
        buzzer1=0.0040
        music(buzzer1)
