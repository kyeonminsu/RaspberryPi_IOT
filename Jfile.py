class file_str:
    def J_file_write(self):
        fle=open('text.txt', 'w')
        for i in range(1, 101, 1): 
            fle.writelines("%d J is the Genius\n" %(i))
    
        fle.close()

    def J_file_Copy(self):
        fle=open('text.txt', 'r')
        fle2=open('copy.txt', 'w')
        #lst=list()
        while True:
            wrd =fle.readline()
            fle2.writelines(wrd)
            if(wrd==''):
                print("read all End")
                break
            #lst.append(wrd) 
            
            
        fle.close()
        fle2.close()
