import pandas as pd
import matplotlib.pyplot as plt

# df = pd.DataFrame({'day1':[7,1,5,6,3,9,5,8],
#                    'day2':[1,2,8,4,6,5,3,1]})
# print(df)
#
# plt.plot(df)
# lg = plt.legend(['day1','day2'],loc=1, title='t_legend', title_fontsize=14)
# print(lg)
# lg._legend_box.sep = 20 #legendtitle 과 legends 사이 간격
# plt.show()

# plt.plot([2,3,5,9], label='values')
# plt.legend(loc=(0.2,0.5)) #x = 1, y = 1 로 기준을잡고 위치설정해줄수있음
# plt.show()

plt.plot([2,3,5,9], label='values1')
plt.plot([8,1,7,3], label='values2')
plt.plot([5,6,9,5], label='values3')
plt.plot([7,5,8,4], label='values4')
plt.legend(loc=2, ncol=3)
plt.show()

