'''
class file_str:
    def __init__(self):
        self.fleWrite=open('text.txt', 'w')
        self.fleRead=open('text.txt', 'r')
        
    def file_write(self):
        fle=open('text.txt', 'w')
        for i in range(1, 101, 1): 
            fle.writelines("%d Test Successful\n" %(i))
        print("file write success")
       
        
    #server txtfile
    def file_write2(self, data):
        self.fleWrite.writelines(data)
        
    def file_read(self):      
        data=self.fleRead.readline()
        return data

    def file_close(self):
        self.fleWrite.close()
        self.fleRead.close()
'''
