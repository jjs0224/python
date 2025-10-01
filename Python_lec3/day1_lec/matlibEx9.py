import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-4, 4, 1024)
y = 0.25 * (x * 4) * (x + 1) * (x - 2)
#
# plt.annotate('annotate text',
#              ha='left', va='bottom',
#              xytext=(-1.5, 20), #텍스트시작점 위치
#              xy=(1.75, -2.8), #화살표끝이 가르키는 위치
#              arrowprops={'facecolor':'r', 'shrink':0.1})
#             #화살표색상(facecolor), shrink=0.1=>10%줄여줌. 옵션은 엄청많음!
# plt.plot(x, y, c='k')
# plt.show()

align_test = ['center','left','right']

ax1 = plt.gca() #get current axes
ax1.axes.get_xaxis().set_visible(False)
ax1.axes.get_yaxis().set_visible(False)

for i, align in enumerate(align_test):
    plt.text(0, i, f'align={align}', ha=align, fontsize=14)
    #
plt.plot([0,0], [-1, len(align_test)], c='#808000', ls='--')
#vertical line (x=0, y= -1 -> 3)
plt.scatter([0] * len(align_test), range((len(align_test))))
#draw 3 dots starting from yaxis=0, 1, 2
plt.show()
