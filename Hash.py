class Hash:
    def __init__(self,value,key):
        self.key=key
        self.value=value

def Hashing(self,value):
    self=Hash(value)
    
#str(a)[len(str(a))-1:] mod
def Hash_function(value):
    value=float(value)/3
    key=int(str(value)[len(str(value))-1:])
    a=('n'+str(key))
    Hashing(a,value)
    
