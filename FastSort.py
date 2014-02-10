
step=0
def fast(arr,left,right,step):
	i=left
	j=right
	m=arr[(right+left)/2]
	if (left<right):
		while (i<j):
			while (arr[i]<m): 
				i+=1
			while (arr[j]>m):
				j-=1
			if (i<=j):
				temp=arr[i]
				arr[i]=arr[j]
				arr[j]=temp
				i+=1
				j-=1
				step+=1
		if (i<right):
			fast(arr,i,right,step)
		if (left<j):
			fast(arr,left,j,step)
	return arr,step
