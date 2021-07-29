import socket
from operator import eq
import sys

print("start!")
com_socket=socket.socket()
com_socket.bind(('127.0.0.1',2561))

com_socket.listen(10)
connection, address = com_socket.accept()
print(address, "Connected good")
fle=open('1234.jpg','wb')
arr=bytearray()
i=1
str1='Q'
while True:
    image=connection.recv(1024).decode("UTF-8")
    if(eq(image, str1)):
        arr=image
        fle.write(arr)
        connection.close()
        print("End")
        break
    """
    if(len(image)<1024):
        arr=image
        fle.write(arr)
        connection.close()
        print("End")
        break
    """  
    arr=image
    fle.write(arr)
    print(i)
    i=i+1
    image2=0


fle.close()
