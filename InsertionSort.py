import random

def fileimport(filename):
	a = (open(filename).read()).split(" ")
	return a

def insertion_sort(l):
	count=0
	for i in xrange(1, len(l)):
		print l
		j = i - 1
		value = l.pop(i)
		while (j >= 0) and (l[j] > value):
			j = j- 1
		count+=1
		l.insert(j + 1, value)
	return l,count
def randomize(a,l):
	for i in range (l):
		z=random.randint(1,50)
		a.append(z)
	return a

def write_file(filename,a):
		f=open(filename,'w')
		for i in range (len(a[0])):
			f.write(str(a[0][i]))
			f.write(" ")
		f.write("\n")	
		f.write(str(a[1]))
		f.close()
a=[]
#randomize(a,10)
#b=insertion_sort(a)
#write_file("out.txt",b)