import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

from sub.field import field

matplotlib.rcParams['font.family'] ='Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] =False

# 0: 주식 가치와 완전히 동일하다.(따로 그래프 그릴 필요 없음)
# 3: 한 턴이 끝날때마다 돈을 잃는 수 밖에 없다.
# 4: 비현실적으로 현금이 많이 투입
# 5: 단순매수가 낫다. 
# 6: 돈을 잃는 경우밖에 없는 최악의 선택
# 7: 비현실적으로 현금이 많이 투입, 투입대비 성능 최악
# 0,1,2,8,9,10,11: 그나마 현실적이다. 
#   - 0: 현금 처음에만 필요
#   - 1: 현금 계속 투입됨
#   - 8: 떨어질 때 level을 조정 안하면 오른 이유가 전혀 없다.
#   - 2, 8, 9: level을 조정 안하면 오른 이유가 전혀 없다.
#   - 10,11: 초기비용의 2~3배
# 다 보면 아마 2번이 제일 낫지않나 싶다.
strategynumber = 11
strategyname=[
'0. 단순매수', 
'1. 적금식', 
'2. 리벨런싱', 
'3. 오를수록사두고,펀드에돈다떨어지면다시처음만큼사두기', 
'4. 손해를용납못하는스타일', 
'5. 추매를용납못하는스타일', 
'6. level을올리고일정수준이하일때파는스타일,같아지면다시사기', 
"7. '항상이기는법'방법", 
'8. 리벨런싱,떨어 질때만', 
'9. 리벨런싱떨어질때만,level업데이트', 
'10. 리벨런싱 떨어질때와 엄청 올랐을 때',
'11. 담배값 적금',
'12. 월적금',
'13. 레벨 = 인플레이션, 떨어질 때는 월적금, 오를때는 리벨런싱 ( 하이브리드 )'
]

# marketnumber, startpoint, israw : res폴더에 있는 마켓 샘플 초기 설정
marketnumber, startpoint, israw = "ni225", 6000, True

# fisrtput, firstprice = 초기 투입 자산, 초기 마켓 가격
fisrtput, firstprice = 10, 10

x,y,z,w = [],[],[],[]

# lim은 샘플의 크기, forcount는 for문의 횟수
lim = 5000

############################################## 번호 #######################################################

f = field(fisrtput, firstprice, lim)
f.setmarket(marketnumber, startpoint, israw = israw)
for time in range(lim):
	f.next(strategynumber)
	y.append(f.getinfo(object = 'm'))
	z.append(f.getinfo()/f.getinfo(cate = 'cash'))
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

############################################## 번호 #######################################################
'''

2.


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