import matplotlib.pyplot as plt
import numpy as np

# x = np.linspace(-np.pi, np.pi, 256)
# y = np.cos(x)
# plt.plot(x, y)
# plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
#            ['-pi','-pi/2','0','pi/2','pi'])
# #xticks (해당하는 틱을 (x.values) 지정해줌 => 여기서는 파이값으로)
# #xticks(labels [] => 숫자대신 문자열로 처리
# plt.yticks([-1,0,1],
#            ['low','zero','high'])
# #y axis 값도 바꿔줄수있음
# plt.grid(True) #선들을 틱에 맞춰서 그림
# plt.show()

data = np.arange(0, 5, 0.2)
plt.title('using single plot to draw more than 1 line')
plt.plot(data, data, 'b--', data, 0.1*data**2, 'go:', data, 0.1*data**3, 'rs-')
#3가지 다른 줄을 그리고싶을때 (x,y,style,   x,y,style,    x,y,style)
plt.show()

# plt.title('defining and using plot for each line')
# plt.plot([10,20,30,40],[4,2,9,12],
#          color='k', lw=4, ls='--', marker='o', ms=12, mec='blue', mew=5, mfc='yellow')
# plt.plot([10,20,30,40],[22,7,15,2],
#          color='red', lw=4, ls='--', marker='o', ms=12, mec='yellow', mew=5, mfc='blue')
# plt.show()
























