import matplotlib.pyplot as plt
import numpy as np

np.random.seed(777)
plot_data1 = np.random.randn(50).cumsum()
plot_data2 = np.random.randn(50).cumsum()
plot_data3 = np.random.randn(50).cumsum()
plot_data4 = np.random.randn(50).cumsum()

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.set_title('Line Plots: Markers, Colors, and Linestyles')
ax1.plot(plot_data1, color='blue', ls='-', marker='o')
ax1.plot(plot_data2, color='red', ls='--', marker='+')
ax1.plot(plot_data3, color='green', ls='-.', marker='*')
ax1.plot(plot_data4, color='orange', ls=':', marker='s')

#tick 위치 바꿔줄수있음.. 이건 add_subplot() 사용해야 사용가능!plt.엔 불가능
ax1.xaxis.set_ticks_position('top')
ax1.yaxis.set_ticks_position('right')

plt.legend(['Blue Solid','Red Dashed','Green Dash Dot','Orange Dotted'],
           loc=1)
plt.xlabel('Draw')
plt.ylabel('Random Number')

# plt.plot(plot_data1, 'b-o',
#          plot_data2, 'r--+',
#          plot_data3, 'g-.*',
#          plot_data4, 'y:s')
plt.savefig('line_plot_quiz.png', dpi=400, bbox_inches='tight')
plt.show()