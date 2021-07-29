#import kyeonminsu201510045class
from midterm import kyeonminsu201510045class


print("Start!!")
clsSock=kyeonminsu201510045class.midterm()
clsSock.server_socket('192.168.0.2',5550)
print("Client -> Server Connected!!")

while True:
    recv_data=clsSock.Receive()
    if(recv_data=='Q'):
        break
    print(recv_data)
    send_data = input("message : ")
    clsSock.Send(send_data)

print("END")
