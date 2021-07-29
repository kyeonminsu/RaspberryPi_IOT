from midterm import kyeonminsu201510045class

print("Start!!")
clsSock=kyeonminsu201510045class.midterm()
clsSock.client_socket('192.168.0.2',5550)
print("Client -> Server Connected!!")

while True:
    send_data = input("message : ")
    clsSock.Send(send_data)
    if(send_data=='Q'):
        break
        
    recv_data=clsSock.Receive()
    print(recv_data)


print("END")
