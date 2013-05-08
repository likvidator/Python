class Hash:
    def __init__(self,value,key):
        self.key=key
        self.value=value
class Hash_table:
    def __init__(self):
        self.n0=None
        self.n1=None
        self.n2=None
        self.n3=None
        self.n4=None
        self.n5=None
        self.n6=None
        self.n7=None
        self.n8=None
        self.n9=None
    def Hash_function(self,value):
        ch=float(value)/3
        key=int(str(ch)[len(str(ch))-1:])
        if key==0:
            self.n0=Hash(value,key)
        if key==1:
            self.n1=Hash(value,key)
        if key==2:
            self.n2=Hash(value,key)
        if key==3:
            self.n3=Hash(value,key)
        if key==4:
            self.n4=Hash(value,key)
        if key==5:
            self.n5=Hash(value,key)
        if key==6:
            self.n6=Hash(value,key)
        if key==7:
            self.n7=Hash(value,key)
        if key==8:
            self.n8=Hash(value,key)
        if key==9:
            self.n9=Hash(value,key)
        return (self)
    def search(self,value):
        ch=float(value)/3
        key=int(str(ch)[len(str(ch))-1:])
        write=Hash(None,None)
        if key==0:
            write=self.n0
        if key==1:
            write=self.n1
        if key==2:
            write=self.n2
        if key==3:
            write=self.n3
        if key==4:
            write=self.n4
        if key==5:
            write=self.n5
        if key==6:
            write=self.n6
        if key==7:
            write=self.n7
        if key==8:
            write=self.n8
        if key==9:
            write=self.n9
        if write.key==None:
            print ("No")
        else:
            print ('Yes','key=',write.key)
def Hashing(self,value):
    self=Hash(value)
    
#str(a)[len(str(a))-1:] # mod
def Hash_function(self,value):
    ch=float(value)/3
    key=int(str(ch)[len(str(ch))-1:])
    if key==0:
        self.n0=Hash(value,key)
    if key==1:
        self.n1=Hash(value,key)
    if key==2:
        self.n2=Hash(value,key)
    if key==3:
        self.n3=Hash(value,key)
    if key==4:
        self.n4=Hash(value,key)
    if key==5:
        self.n5=Hash(value,key)
    if key==6:
        self.n6=Hash(value,key)
    if key==7:
        self.n7=Hash(value,key)
    if key==8:
        self.n8=Hash(value,key)
    if key==9:
        self.n9=Hash(value,key)
    return (self)
    
