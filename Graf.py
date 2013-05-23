def printmatrix(N):
	for i in range(len(N)):
		print N[i]
# def Deicstra(N,a,b):
# 	d=N
# 	s=[]
# 	for i in range(len(N)):
# 		s+=[0]
# 	mark=[]
# 	for i in range(len(N)):
# 		mark+=[False]
# 	s=d[a-1]
# 	mark[a-1]=True
# 	for n in range(len(N)):
# 		for i in range(len(N)):
# 			if (s[i]<d[n][i]) and not(mark[i]) :
# 				s[i]=d[n][i]
# 		markcd[n]=True
# 	print s[b-1]
def Floida(N):
	s=N
	for k in range(len(s)):
		for i in range(len(s)):
			for j in range(len(s)):
				s[i][j]=min(int(s[i][j]),int((s[i][k])+(s[k][j])))
	return s
def fileimport():
	f=open('textgraf.txt', 'r')
	a=f.read()
	i=[]
	j=[]
	n=0
	s=''
	while n< len(a):
		if not(a[n]==',') and not (a[n]=="\n"):
			#i.append(int(a[n]))
			s+=str(a[n])
		elif (a[n]==','):
			i.append(int(s))
			s=''
		elif (a[n]=="\n"):
			i.append(int(s))
			j.append(i)
			i=[]
			s=''
		n+=1
	f.close()
	return(j)


def write_file(N):
        f=open('Graf.txt','w')
        f.write("digraph G{ ")
        write_for_graphviz(f,N)
        f.write("}")
        f.close()



def write_for_graphviz(f,N):           
	for i in range(len(N)-1):
		for j in range(i+1,len(N)-1):
			f.write (str(i))
			f.write ("->")
			f.write (str(j))
			f.write ("[label=")
			f.write (str(N[i][j]))
			f.write ("]")
			f.write ('\n')

	
		






	

	



	
