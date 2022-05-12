import random
import math

from . import possetion

class strategy:
	time, currentprice = 0, 0
	p = None

	memorylist=[]
	memoryvar, subvar = 0, 0

	def __init__(self, fund,price):
		self.p = possetion.possetion(fund,price)
	
	def setprice(self, price):
		self.currentprice = price
		self.p.setprice(price)


	#13. 레벨 = 인플레이션, 떨어질 때는 월적금, 오를때는 리벨런싱 ( 하이브리드 )
	def strategy13(self):
		fund = self.p.getinfo(cate = 'fund')
		if self.time==0:
			self.memoryvar = fund
			self.subvar = fund
		else:
			if fund<self.memoryvar:
				self.p.buy(0.05)
			elif fund>1.2*self.memoryvar:
				self.p.sell(fund-self.memoryvar)
		self.memoryvar *= math.pow(1.02,1/250)
		self.time+=1


	#12. 월 적금
	def strategy12(self):
		if self.time==0:
			self.memoryvar = self.p.getinfo(cate = 'fund')
		elif self.time%1000 == 0 :
			self.p.buy(self.memoryvar)
		self.time+=1

	#11. 담배값 적금
	def strategy11(self):
		if self.time==0:
			self.memoryvar = self.p.getinfo(cate = 'fund')/1000
		else:
			self.p.buy(self.memoryvar)
		self.time+=1

	#10. 리벨런싱 떨어질때와 엄청 올랐을 때 ( 하이브리드 )
	def strategy10(self):
		fund = self.p.getinfo(cate = 'fund')
		if self.time==0:
			self.memoryvar = fund
			self.subvar = fund
		else:
			if fund<self.memoryvar*0.9:
				self.p.buy(self.memoryvar-fund)
			elif fund>self.subvar:
				self.subvar = fund
			elif fund<self.subvar*0.9:
				self.p.sell(fund-self.memoryvar)
				self.subvar = self.memoryvar
		self.time+=1

	#9. 리벨런싱, 떨어질때만, level 업데이트
	def strategy9(self):
		fund = self.p.getinfo(cate = 'fund')
		if self.time==0:
			self.memoryvar = fund
		else:
			if fund<self.memoryvar*0.9:
				self.p.buy(self.memoryvar-fund)
				self.memoryvar = fund
		self.time+=1

	#8. 리벨런싱, 떨어질때만
	def strategy8(self):
		fund = self.p.getinfo(cate = 'fund')
		if self.time==0:
			self.memorylist.append(fund)
		else:
			if fund<self.memorylist[0]*0.8:
				self.p.buy(self.memorylist[0]-fund)
		self.time+=1

	#7. '항상 이기는 법' 방법
	def strategy7(self):
		fund = self.p.getinfo(cate = 'fund')
		if self.time==0 or fund > 1000:
			self.memoryvar = fund
		else:
			if fund>self.memoryvar:
				self.p.buy(fund*0.1)
			elif self.memoryvar<fund:
				self.p.sell(fund)
			elif fund==0:
				self.p.buy(10)
			self.memoryvar = self.p.getinfo(cate = 'fund')
		self.time+=1

	#6. level을 올리고 일정수준 이하일때 파는 스타일, 같아지면 다시 사기
	def strategy6(self):
		fund = self.p.getinfo(cate = 'fund')
		if self.time==0:
			self.memoryvar = fund
		else:
			if fund>self.memoryvar:
				self.memoryvar = fund
				self.subvar = self.currentprice
			elif fund < 0.1 and self.currentprice>self.subvar:
				self.p.buy(self.memoryvar)
			elif self.memoryvar*0.9>fund:
				self.p.sell(fund)
		self.time+=1

	#5. 추매를 용납 못하는 스타일
	def strategy5(self):
		fund = self.p.getinfo(cate = 'fund')
		if self.time==0:
			self.memoryvar = fund
		else:
			if fund>self.memoryvar:
				self.p.sell(fund-self.memoryvar)
			else:
				self.memoryvar = fund
		self.time+=1

	#4. 손해를 용납 못하는 스타일
	def strategy4(self):
		fund = self.p.getinfo(cate = 'fund')
		if self.time==0:
			self.memoryvar = fund
		else:
			if fund<self.memoryvar:
				self.p.buy(self.memoryvar-fund)
			else:
				self.memoryvar = fund
		self.time+=1

	#3. 오를 수록 사두고, 펀드에 돈 다 떨어지면 다시 처음만큼 사두기
	def strategy3(self):
		fund = self.p.getinfo(cate = 'fund')
		if self.time==0:
			self.memorylist.append(fund)
		elif fund<0.1:
			self.p.buy(self.memorylist[0])
		else:
			if fund>self.memoryvar:
				self.p.buy(fund-self.memoryvar)
			else:
				self.p.sell(fund/10)

		self.memoryvar = fund
		self.time+=1

	#2. 리벨런싱
	def strategy2(self):
		fund = self.p.getinfo(cate = 'fund')
		if self.time==0:
			self.memorylist.append(fund)
		else:
			if fund>self.memorylist[0]*1.1:
				self.p.sell(fund-self.memorylist[0])
			elif fund<self.memorylist[0]*0.9:
				self.p.buy(self.memorylist[0]-fund)
		self.time+=1

	#1. 적금식
	def strategy1(self):
		self.p.buy(1)

	#0. 단순 매수
	def strategy0(self):
		pass

	def getinfo(self, cate = "whole"):
		return self.p.getinfo(cate)