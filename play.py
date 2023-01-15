import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

from sub.field import field

matplotlib.rcParams['font.family'] ='Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] =False

#
# 롤하지말고 같이 코딩합시다 피방에서 코딩허자
# 여따 
#

# 0: 주식 가치와 완전히 동일하다.(따로 그래프 그릴 필요 없음)
# 3, 4: 비현실적으로 현금이 많이 투입
# 5, 6 < 0
# 7 < 2
# 11 < 12
# 0,2,8,9,10,12,13: 그나마 현실적이다. 
#   - 0: 현금 처음에만 필요
#   - 1: 현금 계속 투입됨
#   - 8: 떨어질 때 level을 조정 안하면 오른 이유가 전혀 없다.
#   - 2, 8, 9: level을 조정 안하면 오른 이유가 전혀 없다.
#   - 10,11: 초기비용의 2~3배
# 다 보면 아마 2번이 제일 낫지않나 싶다.
strategyname=[
'0. 단순매수', 
'X. 적금식 -> 12', 
'2. 리벨런싱', 
'X. 오를수록사두고,펀드에돈다떨어지면다시처음만큼사두기', 
'X. 손해를용납못하는스타일', 
'X. 추매를용납못하는스타일', 
'X. level을올리고일정수준이하일때파는스타일,같아지면다시사기', 
"X. '항상이기는법'방법 -> 2", 
'8. 리벨런싱,떨어 질때만', 
'9. 리벨런싱떨어질때만,level업데이트', 
'10. 리벨런싱 떨어질때와 엄청 올랐을 때',
'11. 담배값 적금',
'12. 월적금',
'13. 레벨=인플레이션&월적금+리벨런싱'
]

# marketnumber, startpoint, israw : res폴더에 있는 마켓 샘플 초기 설정
marketnumber, startpoint, israw = "ni225", 6000, True

# fisrtput, firstprice = 초기 투입 자산, 초기 마켓 가격
fisrtput, firstprice = 10, 10

# investers 
# 이거 숫자바꾸면 됨
investers = [2, 4,5,6, 8, 9, 10, 11, 12, 13]
x,p,y,w = [],[],[],[]

y.append([])
for i in investers:
	y.append([])

# lim은 샘플의 크기, forcount는 for문의 횟수
lim = 8000

############################################## 번호 #######################################################

f = field(fisrtput, firstprice, lim, investers)
f.setmarket(marketnumber, startpoint, israw = israw)
for time in range(lim):
	f.next()
	p.append(100*(f.getinfo('m')/firstprice-1))
	for i in range(len(investers)):
		y[i].append(f.getinfo(i)/f.getinfo(i, cate='cost')*100)

	w.append(100*(fisrtput/firstprice-1))
	fisrtput *= math.pow(1.02,1/250)

x = np.array(range(lim))/250

plt.hlines(0,0,x[-1],label="x-axis", color = 'k')

plt.plot(x, p, label = 'price')
for i in range(len(investers)):
	plt.plot(x, y[i], label = str(strategyname[investers[i]]))
plt.plot(x, w, label = 'interest')

plt.legend(loc = "best", prop={'size': 6})
plt.xlabel("시간 (년)")
plt.ylabel("시작일 기준, 투자 대비 산출 (%) ")
plt.title(marketnumber+": startpoint = "+str(startpoint)+", lim = "+str(lim))
plt.show()

############################################## 번호 #######################################################
'''
3. 수익률 ( 투자 대비 산출 )

f = field(fisrtput, firstprice, lim, investers)
f.setmarket(marketnumber, startpoint, israw = israw)
for time in range(lim):
	f.next()
	p.append(100*(f.getinfo('m')/firstprice-1))
	for i in range(len(investers)):
		y[i].append(f.getinfo(i)/f.getinfo(i, cate='cost')*100)

	w.append(100*(fisrtput/firstprice-1))
	fisrtput *= math.pow(1.02,1/250)

x = np.array(range(lim))/250

plt.hlines(0,0,x[-1],label="x-axis", color = 'k')

plt.plot(x, p, label = 'price')
for i in range(len(investers)):
	plt.plot(x, y[i], label = str(strategyname[investers[i]]))
plt.plot(x, w, label = 'interest')

plt.legend(loc = "best", prop={'size': 6})
plt.xlabel("시간 (년)")
plt.ylabel("시작일 기준, 투자 대비 산출 (%) ")
plt.title(marketnumber+": startpoint = "+str(startpoint)+", lim = "+str(lim))
plt.show()

2. 실제 수익

f = field(fisrtput, firstprice, lim, investers)
f.setmarket(marketnumber, startpoint, israw = israw)
for time in range(lim):
	f.next()
	p.append(f.getinfo('m')-firstprice)
	for i in range(len(investers)):
		y[i].append(f.getinfo(i))

	w.append(fisrtput-firstprice)
	fisrtput *= math.pow(1.02,1/250)

x = np.array(range(lim))/250

plt.hlines(0,0,x[-1],label="x-axis", color = 'k')

plt.plot(x, p, label = 'price')
for i in range(len(investers)):
	plt.plot(x, y[i], label = str(strategyname[investers[i]]))
plt.plot(x, w, label = 'interest')

plt.legend(loc = "best", prop={'size': 6})
plt.xlabel("시간 (년)")
plt.ylabel("수익, 초기 투입: "+str(firstprice))
plt.title("imi stock!")
plt.show()

1.

f = field(fisrtput, firstprice, lim)
f.setmarket(marketnumber, startpoint, israw = israw)
for time in range(lim):
	f.next(strategynumber)
	y.append(f.getinfo(object = 'm'))
	z.append(f.getinfo())
	w.append(fisrtput)
	fisrtput *= math.pow(1.02,1/250)

x = np.array(range(lim))/250
y = (np.array(y)-firstprice)
w = (np.array(w)-firstprice)

plt.hlines(0,0,x[-1],label="x-axis", color = 'k')
plt.plot(x, y, label = 'price')
plt.plot(x, z, label = 'invest')
plt.plot(x, w, label = 'interest')
plt.legend(loc = "best")
plt.xlabel("시간 (년)")
plt.ylabel("수익, 초기 투입: "+str(firstprice))
plt.title(strategyname[strategynumber])
plt.show()

'''