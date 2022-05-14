import random
import math

class strategy:
	#13. 레벨 = 인플레이션, 떨어질 때는 월적금, 오를때는 리벨런싱 ( 하이브리드 )
	def strategy13(time, memory):
		trade = 0
		if time == 0:
			memory.append(memory[0])
		else:
			if memory[1]<memory[2]:
				trade = 0.05
			elif memory[1]>1.2*memory[2]:
				trade = -( memory[1]-memory[0] )

			memory[2] *= math.pow(1.02,1/250)

		return trade, memory


	#12. 월 적금
	def strategy12(time, memory):
		if time%1000 == 0:
			trade = memory[0]
		else:
			trade = 0

		return trade, memory

	#11. 담배값 적금
	def strategy11(time, memory):
		trade = memory[0]/1000
		return trade, memory

	#10. 리벨런싱 떨어질때와 엄청 올랐을 때 ( 하이브리드 )
	def strategy10(time, memory):
		trade = 0
		if time==0:
			memory.append(memory[0])
		else:
			if memory[1]<memory[0]*0.9:
				trade = memory[0]-memory[1]
			elif memory[1]>memory[2]:
				memory[2] = memory[1]
			elif memory[1]<memory[2]*0.9 and memory[1]>memory[0]:
				trade = -( memory[1]-memory[0] )
				memory[2] = memory[0]

		return trade, memory

	#9. 리벨런싱, 떨어질때만, level 업데이트
	def strategy9(time, memory):
		trade = 0
		if time==0:
			memory.append(memory[0])
		else:
			if memory[1]<memory[2]*0.9:
				trade = memory[0]-memory[1]
				memory[2] = memory[1]

		return trade, memory

	#8. 리벨런싱, 떨어질때만
	def strategy8(time, memory):
		trade = 0
		if memory[1]<memory[0]*0.8:
			trade = memory[0]-memory[1]

		return trade, memory

	#7. '항상 이기는 법' 방법
	def strategy7(time, memory):
		return strategy2(time, memory)

	#6. level을 올리고 일정수준 이하일때 파는 스타일, 같아지면 다시 사기
	def strategy6(time, memory):
		trade = 0

		# 0 : 초기 fund, 1 : 현재 fund, 2 : 현재 price, 3 : level, 4 : price level, 
		if time==0:
			memory.append(memory[0])
			memory.append(memory[2])
		else:
			# fund가 최고가가 될 때까지 level을 올린다.
			if memory[1]>memory[0]:
				memory[3] = memory[1]
				memory[4] = memory[2]
				
			# fund를 몽땅 판 이후, price가 적당히 비싸질 때까지 기다린다.
			elif memory[1] < 0.1 and memory[2]>memory[4]:
				trade = memory[0]
				
			# fund를 몽땅 판다.
			elif memory[3]*0.9 > memory[1]:
				trade = -( memory[1] )

		return trade, memory

	#5. 추매를 용납 못하는 스타일
	def strategy5(time, memory):
		trade = 0
		if time==0:
			memory.append(memory[0])
		else:
			if memory[1]>memory[2]:
				trade = - ( memory[1] - memory[2] )
			else:
				memory[2] = memory[1]

		return trade, memory

	#4. 손해를 용납 못하는 스타일
	def strategy4(time, memory):
		trade = 0
		if time==0:
			memory.append(memory[0])
		else:
			if memory[1]<memory[2]:
				trade = memory[2] - memory[1] 
			else:
				memory[2] = memory[1] 

		return trade, memory

	#3. 오를 수록 사두고, 펀드에 돈 다 떨어지면 다시 처음만큼 사두기
	def strategy3(time, memory):
		trade = 0
		if memory[1]<0.1:
			trade = memory[0]
		elif memory[1]>memory[0]:
			trade = memory[1]-memory[0]
		else:
			trade = -( memory[1]/50 )
		memory[0] = memory[1]

		return trade, memory

	#2. 리벨런싱
	def strategy2(time, memory):
		trade = 0
		if memory[1]>memory[0]*1.1:
			trade = -( memory[1]-memory[0] )
		elif memory[1]<memory[0]*0.9:
			trade = memory[0] - memory[1]

		return trade, memory

	#1. 적금식
	def strategy1(time, memory):
		return strategy.strategy12(time, memory)

	#0. 단순 매수
	def strategy0(time, memory):
		pass