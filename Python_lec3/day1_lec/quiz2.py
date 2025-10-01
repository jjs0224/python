import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
plt.rc('font', family='Malgun Gothic' )

data = pd.read_csv('tips.csv')
print(data)
xrange = range(len(data))
data1 = data['total_bill']
data2 = data['tip']

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_title('결재 금액과 Tip(이중 측)')
color = 'tab:red' #tab: tableau color from matplotlib.org color map 참조

ax1.set_ylabel('결재 금액', color=color)
ax1.plot(data1, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('팁(tip)', color=color, rotation=0) #rotation=0이 가로위치
ax2.plot(data2, color=color)
ax2.tick_params(axis='y', labelcolor=color, labelrotation=270, labelsize=15)
fig.tight_layout()
plt.show()


#
# ax1 = plt.gca()
# ax2 = ax1.twinx()
#
# bill_line = ax1.plot(data1, color='red', lw=1)
# ax1.set_ylabel('결재금액', color='red')
# ax1.tick_params(axis='y', labelcolor='red')
# tip_line = ax2.plot(data2, color='blue', lw=1)
# ax2.set_ylabel('팁(tip)', color='blue', rotation=0)
# ax2.tick_params(axis='y',  labelrotation=270, labelcolor='blue', rotation=270)
# plt.title('결재 금액과 Tip(이중 축')
# plt.show()

