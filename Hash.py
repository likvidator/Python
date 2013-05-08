class init:
    def __init__(self,value,key):
        self.key=key
        self.value=value

def Hashing(value):
    summ=0
    for n in str(value):
        summ+=int(ord(n))
    return (summ%10)

class Hash:
    def __init__(self):
        self.array=[]
        for i in range(10):
            self.array+=[init(1,2)]
    def add(self,value):
        key=Hashing(value)
        self.array[key].key=key
        self.array[key].value=value
    def delite(self,value):
        key=Hashing(value)
        if self.array[key].value!=None:    
            self.array[key].key=None
            self.array[key].value=None
            print "True"
        else:
            print "No Delite"
    def search(self,value):
        key=Hashing(value)
        if self.array[key].value!=None:    
            print ("Yes Key=",self.array[key].key)
        else:
            print "No"


        
