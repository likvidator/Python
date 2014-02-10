import curses
import numpy
import time
stdscr = curses.initscr()
curses.curs_set(0)
stdscr.keypad(1)
#stdscr.border(0)
curses.start_color()
val=0
a=numpy.zeros((20,20),"int")
Status=True
a[6][2]=7
a[2][2]=8
a[5][3]=6
a[2][7]=6
a[2][4]=6
a[4][2]=6
a[15][16]=6
a[13][5]=6
a[6][16]=6
a[19][1]=6
a[12][3]=6
a[5][1]=1
a[5][2]=1
a[5][3]=1
a[5][4]=1
a[5][5]=1
a[5][6]=1
zn=1

# def info():
	# stdscr.addstr((len(a)+2),0, str("up=u"))
	# stdscr.addstr((len(a)+3),0, str("down=j"))
	# stdscr.addstr((len(a)+4),0, str("left=h"))
	# stdscr.addstr((len(a)+5),0, str("right=k"))
	# stdscr.addstr((len(a)+6),0, str("exit=q"))

def search(a,z):
	for i in range(len(a)):
		for j in range(len(a)):
			if a[i][j]==z:
				return i,j
def zabor(a):
	for i in range(len(a)):
		for j in range(len(a)):
			if (i==0) or (j==0) or (i==len(a)-1) or (j==len(a)-1):
				a[i][j]=1
def printmatrix(a):
	z=''
	for i in range(len(a)):
		for j in range(len(a)):
			if a[i][j]==0:
				z+=str(" ")
			if a[i][j]==1:
				z+=str('''#''')
			if a[i][j]==7:
				z+=str(0)
			if a[i][j]==6:
				z+=str('''*''')
			if a[i][j]==8:
				z+=str('z')
			
			z+=str(" ")
			
		z+="\n"
	return (z)
def inputekey():
	while True:

		c = stdscr.getch()

		bot()

		refresh()
		if (c!=10) and (c!=-1):
			return c
def refresh():
	stdscr.addstr(0,0, (printmatrix(a)))
	stdscr.addstr(2,(len(a)*2)+3, str("Star="+str(val)))
	stdscr.refresh()
	# info()
zabor(a)
refresh()
def bot():
	global zn
	i,j=search(a,8)
	if (i==len(a)-2) or (j==len(a)-2) or (i==1) or (j==1):
		zn=zn*(-1)
	a[i][j]=0
	a[i][j+(zn)*1]=8



while Status:
	c = inputekey()
	if c==ord("q"):
		Status=False
	#up
	if c==ord("u"):
		i,j=search(a,7)
		if a[i-1][j]==6:
			val+=1
		if a[i-1][j]!=1:
			a[i][j]=0
			a[i-1][j]=7
			refresh()
	#down
	if c==ord("j"):
		i,j=search(a,7)
		if a[i+1][j]==6:
			val+=1
		if a[i+1][j]!=1:
			a[i][j]=0
			a[i+1][j]=7
			refresh()
	#left
	if c==ord("h"):
		i,j=search(a,7)
		if a[i][j-1]==6:
			val+=1
		if a[i][j-1]!=1:
			a[i][j]=0
			a[i][j-1]=7
			refresh()
	#right
	if c==ord("k"):
		i,j=search(a,7)
		if a[i][j+1]==6:
			val+=1
		if a[i][j+1]!=1:
			a[i][j]=0
			a[i][j+1]=7
			refresh()
	refresh()


time.sleep(0)
curses.curs_set(1)
curses.endwin()
