import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rc('font',family = 'Malgun Gothic')
mpg = pd.read_csv('mpg.csv')
fig = plt.figure(figsize=(12,9))
#grid끼리 너무붙어있어서 xlabel, ylabel 이 안보일수도있으니 hspace(horizontal space), wspace 통해 간격넓혀주기
grid = plt.GridSpec(4,4, hspace=0.7, wspace=0.4)
ax_main = fig.add_subplot(grid[:-1, :-1])
ax_right = fig.add_subplot(grid[:-1, -1], xticklabels=[], yticklabels=[]) #x,y tick 없애기
ax_bottom = fig.add_subplot(grid[-1, :-1],xticklabels=[], yticklabels=[]) #x,y tick 없애기

#data를 mpg 라고 지정해주고 거기서 'displ'는 x값으로,,,, 'hwy'는  y값으로 지정해줌
ax_main.scatter('displ', 'hwy', data=mpg, edgecolors='k')
ax_bottom.hist(mpg.displ, bins=40, color='orange')
#y측 뒤집어줌(위에서 밑으로 데이터가 향하게)
ax_bottom.invert_yaxis()

ax_right.hist(mpg.hwy, bins=40, color='darkblue', orientation='horizontal')

#tick 방향 설정해주기 .yaxis.tick_right() 함수사용하면 바로 오른쪽으로 설정됨
ax_main.yaxis.tick_right()
ax_main.set_xlabel('엔진 크기')
ax_main.set_ylabel('마일 수')
ax_main.set_title('grid Spec Use', fontsize=17)



plt.show()





































