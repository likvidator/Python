def Hashing(value):
    summ=0
    for n in str(value):
        summ+=int(ord(n))
    return (summ%10)




class init:
    def __init__(self,key):
        self.key=key
        self.value=[]
class Hash:
    def __init__(self):
        self.array=[]
        for i in range(10):
            self.array+=[init(None)]
    def add(self,value):
        key=Hashing(value)
        self.array[key].value.append(value)
        self.array[key].key=key
    def delite(self,value):
        key=Hashing(value)
        if self.array[key].value!=None:
            i=0
            while i<=(len(self.array[key].value)-1):
                if self.array[key].value[i]==value:
                    del self.array[key].value[i]
                    print "True"
                i+=1
        else:
            print "No Delite"
    def search(self,value):
        key=Hashing(value)
        if self.array[key].value!=None:
            i=0
            while i<=(len(self.array[key].value)-1):
                if self.array[key].value[i]==value:
                    print "Yes"
                    print self.array[key].value
                    print self.array[key].key
                i+=1

        else:
            print "No"
    def print_hash(self):
        for i in range (len(self.array)):
            print (self.array[i].value,self.array[i].key)
            print ('\n')


n1=Hash() 

