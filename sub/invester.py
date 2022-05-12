import random

from . import strategy

class invester:
	s = None

	def __init__(self, fund,price):
		self.s = strategy.strategy(fund,price)
	
	def setprice(self, price):
		self.s.setprice(price)

		
	def strategy(self,number):	
		#11. 2, 10 섞기
		if number == 13:
			self.s.strategy13()
		#11. 2, 10 섞기
		elif number == 12:
			self.s.strategy12()
		#11. 2, 10 섞기
		elif number == 11:
			self.s.strategy11()

		#10. 리벨런싱 떨어질때와 엄청 올랐을 때
		elif number == 10:
			self.s.strategy10()

		#9. 리벨런싱, 떨어질때만, level 업데이트
		elif number == 9:
			self.s.strategy9()
	
		#8. 리벨런싱, 떨어질때만
		elif number == 8:
			self.s.strategy8()
	
		#7. '항상 이기는 법' 방법
		elif number == 7:
			self.s.strategy7()
	
		#6. level을 올리고 일정수준 이하일때 파는 스타일, 같아지면 다시 사기
		elif number == 6 :
			self.s.strategy6()
	
		#5. 추매를 용납 못하는 스타일
		elif number == 5:
			self.s.strategy5()
	
		#4. 손해를 용납 못하는 스타일
		elif number == 4:
			self.s.strategy4()
	
		#3. 오를 수록 사두고, 펀드에 돈 다 떨어지면 다시 처음만큼 사두기
		elif number == 3:
			self.s.strategy3()
	
		#2. 리벨런싱
		elif number == 2:
			self.s.strategy2()
	
		#1. 적금식
		elif number == 1:
			self.s.strategy1()

		#0. 단순 매수
		elif number == 0:
			self.s.strategy0()

	def getinfo(self, cate = "whole"):
		return self.s.getinfo(cate)