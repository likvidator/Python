def fileimport(filename):
        a=(open(filename).read()).split(" ")
        return a
def search(a,b):
        z=1
        for i in range(len(a)):
                if int(a[i])==b:
                        return z
                z+=1
def binsearch(a,b):        
        max=len(a)
        min=0
        mid=max/2
        z=1
        status='ok'
        if (int(a[mid])==b) :
                status='no'
        while (int(a[mid])!=b) and (status=='ok'):
                z+=1
                if b>int(a[mid]):
                        min=mid
                if b<int(a[mid]):
                        max=mid
                mid=int((max+min)/2)                
        if status=='ok':
                return z
        elif status=='no':
                return 1

def interpolationsearch(a,b):
        max=len(a)-1
        min=0
        mid=max/2
        z=1
        while ((int(a[min])<b) and (int(a[max])>b)):
                z+=1
                mid=min+((b-(int(a[min])))*(max-min)/((int(a[max]))-(int(a[min]))))
                if (a[mid])<b:
                        min=mid+1
                elif (a[mid])>b:
                        max=mid-1
                else:
                        return z
        if (int(a[min])==b):

                return min
        elif (int(a[max])==b):

                return max
        else:

                return -1
# def writefile(filename,z):
#         f=open(filename,'w')
#         f.write(str(z))
#         f.close()
a=fileimport("input.txt")
z=[]
for i in range(len(a)):
        z.append(search(a,int(a[i])))
s=0
for i in range(len(z)):
        s+=(z[i])
search=float(s)/len(z)
z=[]
for i in range(len(a)):
        z.append(binsearch(a,int(a[i])))
s=0
for i in range(len(z)):
        s+=(z[i])
binsearch=float(s)/len(z)
z=[]
for i in range(len(a)):
        z.append(interpolationsearch(a,int(a[i])))
s=0
for i in range(len(z)):
        s+=(z[i])
interpolationsearch=float(s)/len(z)
f=open("output.txt",'w')
f.write("Search "+str(search)+"\n")
f.write("Bin Search "+str(binsearch)+"\n")
f.write("Interpolation Search "+str(interpolationsearch)+"\n")
f.close()