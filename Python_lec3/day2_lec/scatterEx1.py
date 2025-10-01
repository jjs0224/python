import matplotlib.pyplot as plt
import numpy as np

dataA = np.random.randn(100,2)
print(dataA)
dataA += np.array([-1,-1])

dataB = np.random.randn(100,2)
dataB += np.array([1,1])

plt.scatter(dataA[:,0], dataA[:,1], color='0.25')
#0=black, 1=white 색을 숫자로 나타낼수있는데 이건 흑백만가능..
plt.scatter(dataB[:,0], dataB[:,1], color='0.75', edgecolors='k')
#0.75 = 연한회색 이라 색상이 잘안보여서 그럴땐 edgecolors= 사용해서 테두리주기

plt.show()

