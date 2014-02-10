import numpy
import sys
inf=0
def Floida(N):
	s=N
	l=len(s)
	next=numpy.zeros((l,l),"int")
	for k in range(len(s)):
		for i in range(len(s)):
			for j in range(len(s)):
				if ((s[i][k]) + (s[k][j])) < (s[i][j]): 
					s[i][j] = ((s[i][k]) + (s[k][j]))
					next[i][j] = k
				else:
					next[i][j]=-1
				# print k,
				# print " ",
				# print i
				print "Progres",
				print k,
				print " ",
				print i,
				print " ",
				print j
	return(s,next)
def way(N,next,u, v):
   if N[u][v] == 999:
       raise NoPath
   c = u
   while c != v:
     print c
     c = next[c][v]
   print v

def fileimport(filename):
	s=open(filename, 'r').read()
	l=len((open(filename).readline()).split(" "))
	les=len(s)
	arr=numpy.zeros((l,l),"int")
	v=''
	n=0
	i=0
	j=0
	while n< len(s):
		if not(s[n]==' ') and not (s[n]=="\n"):
			v+=str(s[n])
		elif (s[n]==' ') and not(s[n+1]=="\n"):
			if int(v)==0:
				arr[j][i]=inf
			else:
				arr[j][i]=(int(v))
			i+=1
			v=''
		elif (s[n]=="\n"):
			if int(v)==0:
				arr[j][i]=inf
			else:
				arr[j][i]=(int(v))
			i=0
			j+=1               
			v=''
		n+=1
	print "Finish"
	return(arr)
	

def write_matrix(N,filename):
	f=open(filename,'w')
	for i in range(len(N)):
		f.write('\n')
		for j in range(len(N)):
			f.write(str(N[i][j]))
			f.write(' ')

def write_file_gr(N):
        f=open('Graf.txt','w')
        f.write("digraph G{ ")
        write_for_graphviz(f,N)
        f.write("}")
        f.close()



def write_for_graphviz(f,N):           
	for i in range(len(N)):
		for j in range(i+1,len(N)):
			if not(N[i][j]==0):
				f.write (str(i))
				f.write ("->")
				f.write (str(j))
				f.write ("[label=")
				f.write (str(N[i][j]))
				f.write ("]")
				f.write ('\n')
def deykstra(N,node):
    l= len(N)
    if node > l  or node < 0:
        print 'Error'
    else:
        visited = []
        short_dist =[]
        for i in range(l):
            short_dist += [N[node][i]]
            visited += [False]
        visited[node] = True
        for i in range(l):
            m = 0
            for j in range(l):
                if(0 < short_dist[j] < m or m == 0) and not visited[j]:
                    m = short_dist[j]
                    k = j
            visited[k] = True
            for j in range(l):
                if N[k][j] != 0 and (N[k][j] + short_dist[k] < short_dist[j] or short_dist[j] == 0) and not visited[j]:
                    short_dist[j] = N[k][j] + short_dist[k]
        print short_dist
def glub(arr,v):
	mark=new(len(arr[0]))
	Visit=newb(len(arr[0]))
	a=__glub(arr,v,mark,Visit)
	return a
def __glub(arr,v,mark,Visit):
	
	l=len(arr)
	Visit[v]+=1
	mark[v] = True
	for i in range(l):
		if ((arr[v,i]>0) and not(mark[i])):
			Visit=__glub(arr,i,mark,Visit)
	return Visit
def new(a):
	b=[]
	for i in range(a):
		b.append(0)
	return b
def newb(a):
	b=[]
	for i in range(a):
		b.append(False)
	return b
def shir(arr,v):
	l=len(arr)
	a=[]
	mark=new(l)
	Visit=newb(l)
	for i in range(l):
		Visit[i]=0
		mark[i]=False
	Visit[v]+=1
	mark[v]=True
	a.append(v)
	while (len(a)!=0):
		x=a.pop()
		for w in range(l):
			if (arr[x,w])>0 and not(mark[w]):
				mark[w]=True
				Visit[w]+=1
				a.append(w)
	return Visit

# N=fileimport(sys.argv[1])
# b,z=Floida(N)
# write_matrix(b,sys.argv[2])
# write_matrix(z,sys.argv[3])