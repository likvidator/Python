import numpy
step = 0
factorial = lambda x: factorial(x - 1) * x if x > 1 else 1
def quickSort(array):
	print fast(array,0,len(array)-1)
	

def fast(arr,left,right):
	global step
	i=left
	j=right
	m=arr[(right+left)/2]
	if (left<right):
		while (i<j):
			while (arr[i]<m): 
				i+=1
				step+=1
				
			while (arr[j]>m):
				j-=1
				step+=1
				
			if (i<=j):
				temp=arr[i]
				arr[i]=arr[j]
				arr[j]=temp
				i+=1
				j-=1
			
		if (i<right):
			fast(arr,i,right)
		if (left<j):
			fast(arr,left,j)
	return step
def copy(a,b):
	for i in range(len(a)):
		b.append(a[i])
def mass(m):
	arr=[]
	copy(m,arr)
	N=len(arr)
	i=N-2
	while (i>0 and (arr[i]>arr[i+1])):
		i-=1
	if (i>=0):
		j=i+1
		while (j<N-1 and arr[j+1]>arr[i]):
			j+=1
		temp=arr[i]
		arr[i]=arr[j]
		arr[j]=temp
		j=i+1
		while (j<=(N-1+i)/2):
			temp=arr[j]
			arr[j]=arr[N-j+i]
			arr[N-j+i]=temp
			j+=1
	return arr

def start(n):
	global step
	arr=[]
	for i in range(n):
		arr.append(i+1)
	a=[]
	b=[]
	ard=[]
	for i in range(factorial(len(arr))):
		a.append(arr)
		copy(arr,ard)
		step=0
		b.append(fast(ard,0,len(ard)-1))
		ard=[]
		arr=mass(arr)
	return a,b
def serch(a):
	z=max(a)
	for i in range(len(a)):
		if z==a[i]:
			return i
#z,x=start(a)
#z[serch(x)]


