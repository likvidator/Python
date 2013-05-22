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
# 		mark[n]=True
# 	print s[b-1]
def Floida(N,a,b):
	s=N
	for k in range(len(s)):
		for i in range(len(s)):
			for j in range(len(s)):
				s[i][j]=min(int(s[i][j]),int((s[i][k])+(s[k][j])))
	return s[a][b]
def fileimport():
	f=open('textgraf.txt', 'r')
	a=f.read()
	i=[]
	j=[]
	n=0
	while n< len(a):
		if not(a[n]==',') and not (a[n]=="\n"):
			i.append(int(a[n]))
		elif (a[n]=="\n"):
			j.append(i)
			i=[]
		n+=1

	return(j)

	
		






	

	



	
