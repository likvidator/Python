def printmatrix(N):
	for i in range(len(N)):
		print N[i]
# def deykstra(N,node):N
# 		l = len(N)
# 		if node > l  or node < 1:
# 			print 'Error'
# 		else:
# 			node -= 1
# 			visited = []
# 			short_dist =[]
# 			for i in range(l):
# 				short_dist += [N[node][i]]
# 				visited += [False]
# 			visited[node] = True
# 			for i in range(l):
# 				m = 0
# 				for j in range(l):
# 					if(0 < short_dist[j] < m or m == 0) and not visited[j]:
# 						m = short_dist[j]
# 						k = j
# 				visited[k] = True
#                 for j in range(l):
#                     if N[k][j] != 0 and (N[k][j] + short_dist[k] < short_dist[j] or short_dist[j] == 0) and not visited[j]:
#                         short_dist[j] = N[k][j] + short_dist[k]
#             print short_dist
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

	
		






	

	



	
