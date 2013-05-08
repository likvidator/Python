def Hashing(value):
    summ=0
    for n in str(value):
        summ+=int(ord(n))
    return (summ%10)

class init:
    def __init__(self,value,key):
        self.key=key
        self.value=value

class Hash:
    def __init__(self):
        self.array=[]
        for i in range(10):
            self.array+=[init(None,None)]
    def add(self,value):
        key=Hashing(value)
        if self.array[key].key!=None:
            print 'Rewrite',
            print self.array[key].value,
            print '?[Yes/No]'
            messege=raw_input ()
            if messege == 'Yes':
                self.array[key].key=key
                self.array[key].value=value
        else:  
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

    def print_hash(self):
        for i in range (len(self.array)):
            print (self.array[i].value,self.array[i].key)       
            print ('\n')


n1=Hash()      
