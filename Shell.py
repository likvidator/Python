import random

def fileimport(filename):
	a = (open(filename).read()).split(" ")
	return a
#Step=step /2 -1
def shell(arr):
	step=1
	a=[]
	a.append(1)
	
	for i in range(10):
		a.append(3*step+1)
		step=3*step+1
	
	for i in range(len(a)):
		if a[i]>len(arr):
			step=a[i-1]
			break
	print step
	count = 0
	while (step>0):
		for i in range(len(arr)):
			tmp=arr[i]
			j=i-step
			while ((j>=0) and (arr[j]>tmp)):
				arr[j+step]=arr[j]
				j-=step
			count +=1
			arr[j+step]=tmp
			
		step = step /2 -1
	return count-1,arr

#Step=step /3 -1
def shell2(arr):
	step=1
	a=[]
	a.append(1)
	print step
	for i in range(10):
		a.append(3*step+1)
		step=3*step+1
	
	for i in range(len(a)):
		if a[i]>len(arr):
			step=a[i-1]
			break
	
	count = 0
	while (step>0):
		for i in range(len(arr)):
			tmp=arr[i]
			j=i-step
			while ((j>=0) and (arr[j]>tmp)):
				arr[j+step]=arr[j]
				j-=step
			count +=1
			arr[j+step]=tmp
			
		step = step /3 -1
	return count-1,arr

def randomize(a,l):
	for i in range (l):
		z=random.randint(1,50)
		a.append(z)
	return a

def write_file(filename,a):
		f=open(filename,'w')
		f.write(str(a[0]+1))
		f.write("\n")	
		for i in range (len(a[1])):
			f.write(str(a[1][i]))
			f.write(" ")
		f.close()
a=[]
a=randomize(a,10)
b=shell(a)
c=shell2(a)
write_file("text",b)
write_file("text1",c)
