import numpy
import sys

def Floida(N):
	s=N
	l=len(s)
	next=numpy.zeros((l,l),"int")
	for k in range(len(s)):
		for i in range(len(s)):
			for j in range(len(s)):
				if (int(s[i][k]) + int(s[k][j])) < int(s[i][j]): 
					s[i][j] = (int(s[i][k]) + int(s[k][j]))
					next[i][j] = i
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
	l=len(open(filename).readlines())
	arr=numpy.zeros((l,l),"int")
	lines = open(filename).readlines()
	def parse_line(line):
		return map(int,line.split(' '))
	j=map(parse_line,lines)
	for i in range(len(j)):
		for k in range(len(j)):
			arr[i][k]=j[i][k]

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
N=fileimport(sys.argv[1])
b,z=Floida(N)
write_matrix(b,sys.argv[2])
write_matrix(z,sys.argv[3])

	



	
