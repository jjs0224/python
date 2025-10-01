import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rc('font', family='Malgun Gothic')

mpg = pd.read_csv('mpg.csv', encoding='utf-8')
print(mpg)
mpg.info()

# xdata = mpg.loc[:, 'displ'] #'displ' 엔진크기 데이터만 xdata에 지정해주기
# ydata = mpg.loc[:, 'hwy'] #'hwy' 데이터만 ydata 에 지정해주기
#
# plt.plot(xdata, ydata, marker='o', linestyle='None') #xdata, ydata 플롯선언
# plt.title('산점도 그래프', fontsize=15)
# plt.xlabel('엔진 크기')
# plt.ylabel('고속도로 주행마일 수')
# plt.show()
#

print(mpg.drv.unique())

mycolor = ['r','g','b']
label_dict = {'f':'전륜 구동','4':'4륜 구동','r':'후륜 구동'}

for idx, finditem in enumerate(mpg.drv.unique()):
    xdata = mpg.loc[mpg['drv'] == finditem, 'displ']
    ydata = mpg.loc[mpg['drv'] == finditem, 'hwy']
    plt.plot(xdata, ydata,
             color=mycolor[idx],
             marker='o',
             linestyle='None',
             label = label_dict[finditem])

plt.legend(loc='best')
plt.xlabel('엔진 크기')
plt.ylabel('고속도로 주행 마일 수')
plt.grid(True)
plt.show()

