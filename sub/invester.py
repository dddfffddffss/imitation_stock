import random

from sub.strategy import strategy as s
from sub.possetion import possetion

class invester:
	def __init__(self, fund, price, strategynumber):
		self.strategynumber, self.p = strategynumber, possetion(fund,price)
		self.time, self.currentprice = 0, 0
		
		# memoryvar[0] = 가장 처음의 fund, memoryvar[1] = 가장 최근의 fund, 나머지는 각 전략의 memoryvar
		self.memoryvar = [fund, fund]

	def setprice(self, price):
		self.currentprice = price
		self.p.setprice(price)

		
	def next(self):	
		self.memoryvar[1] = self.p.getinfo(cate = 'fund')
		
		#11. 2, 10 섞기
		if self.strategynumber == 13:
			trade, self.memoryvar = s.strategy13(self.time, self.memoryvar)

		#11. 2, 10 섞기
		elif self.strategynumber == 12:
			trade, self.memoryvar = s.strategy12(self.time, self.memoryvar)
		
		#11. 2, 10 섞기
		elif self.strategynumber == 11:
			trade, self.memoryvar = s.strategy11(self.time, self.memoryvar)

		
		#10. 리벨런싱 떨어질때와 엄청 올랐을 때
		elif self.strategynumber == 10:
			trade, self.memoryvar = s.strategy10(self.time, self.memoryvar)

		
		#9. 리벨런싱, 떨어질때만, level 업데이트
		elif self.strategynumber == 9:
			trade, self.memoryvar = s.strategy9(self.time, self.memoryvar)

		
		#8. 리벨런싱, 떨어질때만
		elif self.strategynumber == 8:
			trade, self.memoryvar = s.strategy8(self.time, self.memoryvar)

		
		#7. '항상 이기는 법' 방법
		elif self.strategynumber == 7:
			trade, self.memoryvar = s.strategy7(self.time, self.memoryvar)
	
		
		#6. level을 올리고 일정수준 이하일때 파는 스타일, 같아지면 다시 사기
		elif self.strategynumber == 6 :
			if self.time == 0:
				self.memoryvar.append(self.currentprice)
			else:
				self.memoryvar[2] = self.currentprice
			trade, self.memoryvar = s.strategy6(self.time, self.memoryvar)
	
		
		#5. 추매를 용납 못하는 스타일
		elif self.strategynumber == 5:
			trade, self.memoryvar = s.strategy5(self.time, self.memoryvar)
	
		
		#4. 손해를 용납 못하는 스타일
		elif self.strategynumber == 4:
			trade, self.memoryvar = s.strategy4(self.time, self.memoryvar)
	
		
		#3. 오를 수록 사두고, 펀드에 돈 다 떨어지면 다시 처음만큼 사두기
		elif self.strategynumber == 3:
			trade, self.memoryvar = s.strategy3(self.time, self.memoryvar)
	
		
		#2. 리벨런싱
		elif self.strategynumber == 2:
			trade, self.memoryvar = s.strategy2(self.time, self.memoryvar)
	
		
		#1. 적금식
		elif self.strategynumber == 1:
			trade, self.memoryvar = s.strategy1(self.time, self.memoryvar)

		
		#0. 단순 매수
		elif self.strategynumber == 0:
			trade, self.memoryvar = s.strategy0(self.time, self.memoryvar)

		self.time+=1
		self.p.trade(trade)

	def getinfo(self, cate = "whole"):
		return self.p.getinfo(cate)