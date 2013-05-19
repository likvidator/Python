
#     1,2,3,4,5,6
N = [[0,7,9,4,9,6], # 1
     [7,0,4,3,2,6], # 2
     [9,4,0,8,4,2], # 3
     [4,3,8,0,6,4], # 4
     [9,2,4,6,0,1], # 5
     [6,6,2,4,1,0]] # 6
     
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
def Floida(N):
	s=N
	for k in range(len(s)):
		for i in range(len(s)):
			for j in range(len(s)):
				s[i][j]=min(int(s[i][j]),int((s[i][k])+(s[k][j])))
	printmatrix(s)


	

	



	
