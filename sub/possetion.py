class possetion:
	loss, gain = 0, 0
	f = None

	def __init__(self, money,price):
		self.f = fund(money,price)
		self.loss += money
	
	def setprice(self, price):
		self.f.setprice(price)

	def buy(self,loss):
		self.loss+=loss
		self.f.buy(loss)
		
	def sell(self,gain):
		if self.f.getinfo()>gain:
			self.gain+=gain
			self.f.sell(gain)
		else:
			self.gain+=self.f.getinfo()
			self.f.sell(self.f.getinfo())
	
	def getinfo(self, cate = "whole"):
		if cate == "whole":
			value = self.gain - self.loss + self.f.getinfo()
		elif cate == "fund":
			value = self.f.getinfo()
		elif cate == "cash":
			value = self.gain - self.loss
		
		return value

class fund:
	currentprice, token = 0,0

	def __init__(self,money,price):
		self.token = money/price
	
	def setprice(self, price):
		self.currentprice = price
		
	def buy(self,money):
		self.token+=money/self.currentprice
		
	def sell(self,money):
		self.token-=money/self.currentprice
		
	def getinfo(self):
		return self.currentprice*self.token