class firstclass:
    def add(self, v1,v2):
        return v1+v2
    def sub(self, v1,v2):
        return v1-v2

class Class2(firstclass):
    def __init__(self,v1,v2):
        self.v_1=v1
        self.v_2=v2
    def add2(self, v1):
        return v1+self.v_1
    def sub2(self, v1):
        vl=self.v_2-v1
        return vl

class Class3(Class2):
    def __init__(self,v1,v2,v3):
        Class2.__init__(self,v1,v2)
        self.v_3=v3
    def add(self,v1,v2):
        return v1+v2+self.v_1
    def add3(self,v1,v2=None):
        if v2==None:
            return v1+self.v_3
        else:
            return v1+v2+self.v_3
    def sub3(self, v1):
        return v1-self.v_3+self.v_1

Cls = Class3(20,10,30)
v1=Cls.add(1,2)
v2=Cls.sub(1,2)
v3=Cls.add2(5)
v4=Cls.sub2(5)
print(v1,',',v2,',',v3,',',v4,',',Cls.v_2)
v5=Cls.add3(5)
v6=Cls.add3(5,2)
v7=Cls.sub3(5)
print(v5,',',v6,',',v7)
