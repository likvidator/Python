def Hashing(value,zn):
    summ=0
    for n in str(value):
        summ+=int(ord(n))
    if zn==True:
        return (summ%10)
    if zn==False:
        return (summ)
class init:
    def __init__(self,key,value):
        self.key=[]
        self.value=[]
        self.hashkey=key
class Hash:
    def __init__(self):
        self.array=[]
        for i in range(10):
            self.array+=[init(None,None)]
    def add(self,key,value):
        hashkey=Hashing(key,True)
        self.array[hashkey].value.append(value)
        self.array[hashkey].key.append(key)
        self.array[hashkey].hashkey=hashkey
    def delete(self,key):
        hashkey=Hashing(key,True)
        if self.array[hashkey].value!=None:
            i=0
            while i<=(len(self.array[hashkey].key)-1):
                if self.array[hashkey].key[i]==key:
                    del self.array[hashkey].value[i]
                    del self.array[hashkey].key[i]
                    print "True"
                i+=1
        else:
            print "No Delete"
    def search(self,key):
        hashkey=Hashing(key,True)
        if self.array[hashkey].key!=None:
            i=0
            while i<=(len(self.array[hashkey].key)-1):
                if self.array[hashkey].key[i]==key:
                    return (self.array[hashkey].value[i])
                i+=1
    def print_hash(self):
        for i in range (len(self.array)):
            print (self.array[i].value,self.array[i].key)
            print (self.array[i].hashkey)
            print ('\n')
n1=Hash() 

