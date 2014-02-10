import numpy
import sys
def fileimport(filename):
        integer = ['0','1','2','3','4','5','6','7','8','9']
        lines = open(filename).readlines()
        l = len(lines)
        arr = numpy.zeros((l,l),'int')        
        for i in range(l):
            m = 0
            n = 0
            j = 0
            while j < len(lines[i]):
                k = 1
                ok = False
                while j < len(lines[i]) and lines[i][j] != ' ':
                    if lines[i][j] == '-':
                        k = -1
                    if lines[i][j] in integer:
                        n = n*10 + int(lines[i][j])
                        ok = True
                    j += 1
                j+=1
                if ok:
                    n = n*k
                    arr[i][m] = n
                    n = 0
                    m += 1
            j += 1
        return arr


def determinant(a):
    s=0
    if len(a)==1:
        return a[0][0]
    if len(a)==2:
        det=(a[0][0]*a[1][1])-(a[1][0]*a[0][1])
        return det

    zn=1 
    for i in range(len(a)):
        s+=a[0][i]*zn*determinant(creat(a,i))
        zn=zn*(-1)
    return s    
def creat(a,b):
    arr=numpy.zeros((len(a)-1,len(a)-1),"int")
    z=0
    x=0
    c=range(len(a))
    c.remove(0)
    for i in c:
        for j in range(len(a)):
            if (j!=b)and(z!=len(a))and(x!=len(a)):
                arr[z][x]=a[i][j]
                x+=1
        z+=1
        x=0
    return arr

def write_file(filename,a):
        f=open(filename,'w')
        f.write(str(a))
        f.close()
a=fileimport("input10.txt")
det=determinant(a)
write_file("output.txt",det)