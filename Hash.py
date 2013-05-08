class init:
    def __init__(self,value,key):
        self.key=key
        self.value=value
class Hash:
    def __init__(self):
        self.array=[]
        for i in range(10):
            self.array+=[init(1,2)]
    def add(self,value):
        key=(value % 10)
        self.array[key].key=key
        self.array[key].value=value
    def delite(self,value):
        key=(value % 10)
        if self.array[key].value!=None:    
            self.array[key].key=None
            self.array[key].value=None
            print "True"
        else:
            print "No Delite"
        
        
