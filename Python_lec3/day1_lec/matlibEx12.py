import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
from matplotlib.pyplot import ylabel

# x = np.linspace(-15, 15, 1024)
# y = np.sinc(x)
# ax = plt.gca()
# ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
# ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
# plt.plot(x, y, c = 'k')
# plt.show()

ax = plt.gca()

def make_label(value, pos):
    return f'{100 * value:.1f}'
#function 을 통해서 x-axis 틱 값 정해주기
#--이렇게 사용하면 tick 값 get_xticklabels() 통해 바꿀수있음
ax.xaxis.set_major_formatter(ticker.FuncFormatter(make_label))
x = np.linspace(0, 1, 256)
plt.plot(x, np.exp(-10*x), c='k')

xlabels = ax.get_xticklabels()
plt.setp(xlabels, rotation=30, fontsize=12)
ylabels = ax.get_yticklabels()
plt.setp(ylabels, rotation=90, color='blue')

plt.show()
