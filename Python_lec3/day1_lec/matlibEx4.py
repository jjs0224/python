import matplotlib.pyplot as plt
import numpy as np

plt.title('using legend and changing x-axis, y-axis name')
x = np.linspace(-np.pi, np.pi, 256)
y1, y2 = np.cos(x), np.sin(x)
plt.plot(x, y1, ls='--', label='cosine')
plt.plot(x, y2, ls=':', label='sine')
plt.legend(loc='best')
#legend(범례) 사용하고싶으면 label 값이 꼭! 있어야하고 .legend(loc=위치지정)
# plt.legend(['cos','sin'], loc='best', fontsize=14)
#plot자체에 라벨선언안해주고 legend([레이벨])해줄수도있음=>첫번째 적은라벨부터 적어줌
plt.xlabel('x axis') #x-axis naming to 'x axis'
plt.ylabel('y axis') #y-axis naming to 'y axis'
plt.show()