import matplotlib.pyplot as plt
import numpy as np

# data = np.random.randn(10000)
# plt.boxplot(data) #box 그래프 그릴때 사용되는 함수
# plt.show()

N = 500
normal1 = np.random.normal(loc=100, scale=15, size=N)
normal2 = np.random.normal(loc=88, scale=30, size=N)

fig = plt.figure(figsize=(10,8))
ax1 = fig.add_subplot(111)
#.boxplot(label = []) 통해서 bar 들 이름정해주기
#.boxplot(vert= default is True == 세로모양, False 로바까주면 가로모양으로바뀜(horizontal)
#.boxplot(showmeans=True 평균값어딘지 표시해줌)
ax1.boxplot([normal1, normal2],labels=['normal1','normal2'],vert=False, showmeans=True)
plt.show()