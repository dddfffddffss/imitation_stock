import random
import math
import numpy as np

from . import invester

class field:
	s, m = None, None

	def __init__(self, fund, price, lim):
		self.s, self.m = invester.invester(fund,price), market(price, lim)

	def setmarket(self, marketname, startpoint, israw = False):
		self.m.setmarket(str(marketname), startpoint, israw)

	def next(self,strategy):
		# 1. 가격을 탐색한다
		self.s.setprice(self.m.getprice())

		# 3. 탐색한 가격을 사용한다.
		self.s.strategy(strategy)

		# 3. 마켓이 바뀐다.
		self.m.nextprice()

	def getinfo(self,object = 's', cate = 'whole'):
		if object == 's':
			return self.s.getinfo(cate)
		else:
			return self.m.getinfo()
			
class market:
	price, firstprice = 10.0, 0
	lim, time=0,0
	israw = False
	a = []

	def __init__(self, price, lim):
		self.price = price
		self.firstprice = price
		self.lim = lim
	
	def setmarket(self, marketname, startpoint, israw):
		self.israw = israw
		with open("res\\"+marketname+".txt", "r") as f:
			lines = f.readlines()

		for i in range(startpoint,self.lim+startpoint):
			self.a.append(float(lines[i]))
	
	def getprice(self):
		return self.price
		
	def nextprice(self):
		if self.israw:
			try:
				self.price *= self.a[self.time+1]/self.a[self.time]
			except:
				pass
		else:
			self.price *= self.a[self.time]
		self.time+=1
	
	def getinfo(self):
		return self.price