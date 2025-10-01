import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-4, 4, 1024)
y = 0.25 * (x * 4) * (x + 1) * (x - 2)
plt.plot(x, y, c='k')

box = {
    'facecolor': 'g', #box배경색
    'alpha':0.5, #alpha=투명도 0이랑가까우면 투명함
    'edgecolor':'r', #box border color
    'boxstyle':'round' #box corner = round
}

plt.text(-0.5, 1.25, 'black text mark', fontsize=12,
         bbox=box) #bbox 스타일링을 딕셔너리 통해 지정해줌
plt.show()

