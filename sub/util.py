import math
import numpy as np
import matplotlib.pyplot as plt

def Kurt(array):
    mean = np.mean(array)
    std = np.std(array, ddof = 1)
    n = len(array)
    g2 = n/(n-1)**2*np.sum(((array - mean)/std)**4) - 3
    G2 = ((n-1)/((n-2)*(n-3)))*((n+1)*g2 + 6)
    
    return G2

###################################################################################

def graph(filename):
	with open("res\\"+str(filename)+".txt", "r") as f:
		lines = f.readlines()

	y = []
	for i in lines:
		y.append(float(i))
	
	plt.plot(range(len(lines)),y)
	plt.show()

def writerandom(firstprice, size, filename):
	a=[]
	price = firstprice
	for i in np.random.laplace(0, 0.01, size=size):
		a.append(str(price))
		price *= math.pow(2,i)

	with open("res\\"+str(filename)+".txt", "w") as f:
		f.write("\n".join(a))

def writeinterset(firstprice, interest, size, filename):
	a=[]
	price = firstprice
	for i in range(size):
		a.append(str(price))
		price *= math.pow(1+interest/100,1/250)

	with open("res\\"+str(filename)+".txt", "w") as f:
		f.write("\n".join(a))

def opendata(levelcount):
	with open("res\\ni225.txt", "r") as f:
		lines = f.readlines()

	a=[]
	standard = float(lines[0])
	for i in range(len(lines)-1):
		a.append((float(lines[i+1])-float(lines[i]))/standard)

	a.sort()
	min,max=a[0],a[-1]
	delta = (max - min)/levelcount

	x=[]
	for i in np.arange(min,max,delta):
		x.append(i)

	y=np.zeros(levelcount)
	for i in a:
		if i != max:
			index = int((i-min)/delta)
		else:
			index = levelcount-1
		y[index]+=1
	
	print(Kurt(y))
	print(np.std(a))

	plt.plot(x,y)
	plt.show()

def openrandom(size, levelcount):
	a=[]
	price = 1
	for i in np.random.laplace(0, 0.08, size=size):
		a.append(price)
		price *= math.pow(2,i)

	a.sort()
	min,max=a[0],a[-1]
	delta = (max - min)/levelcount

	x=[]
	for i in np.arange(min,max,delta):
		x.append(i)

	y=np.zeros(levelcount)
	for i in a:
		if i != max:
			index = int((i-min)/delta)
		else:
			index = levelcount-1
		y[index]+=1
	
	print(Kurt(y))
	print(np.std(a))

	plt.plot(x,y)
	plt.show()