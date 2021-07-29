import socket

print("start!!")
com_socket = socket.socket()
com_socket.connect(('127.0.0.1', 2561))

fle=open('1234.jpg', 'rb')
i=1
str2='Q'
while True:
    image=fle.read(1024)
    com_socket.send(bytes(image))
    if(len(image)<1024):
        com_socket.send(bytes(image))
        print("End")
        #com_socket.close()
        break
    
    print(i)
    i=i+1


com_socket.send(bytes(str2, "UTF-8"))
com_socket.close()
fle.close()
