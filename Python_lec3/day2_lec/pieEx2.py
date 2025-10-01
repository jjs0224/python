import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rc('font', family='Malgun Gothic')

data = pd.read_csv('covid_data.csv', index_col='국가')
chartdata = data.loc[['독일','프랑스','중국','영국','이탈리아'],['4월06일','4월07일']]
print(chartdata)
chartdata = chartdata.values #
print(chartdata)

cmap = plt.get_cmap('tab20c')
print(cmap)
print(cmap(np.arange(5)*4)) #인덱스를 떨어트려놓음으로(*4) 칼라차트에서 떨어진색값을가져옴
outer_colors = cmap(np.arange(5) * 4) #outer color 색들 지정
inner_colors = cmap(np.arange(10)) #outer color 색들 지정

INNER_VACANT_CIRCLE_SIZE = 0.3
OUTER_PCTDISTANCE = 0.85
INNER_PCTDISTANCE = 0.75

cum_sum = chartdata.sum(axis=1)
fig, ax = plt.subplots(figsize=(8,8))
ax.pie(cum_sum, radius=1, colors=outer_colors,
       labels=['독일','프랑스','중국','영국','이탈리아'],
       autopct='%.2f%%',
       pctdistance=OUTER_PCTDISTANCE,
       wedgeprops=dict(width=INNER_VACANT_CIRCLE_SIZE, edgecolor='w'))

print(chartdata.flatten())
ax.pie(chartdata.flatten(), radius=1 - INNER_VACANT_CIRCLE_SIZE, colors=inner_colors,
       wedgeprops=dict(width=INNER_VACANT_CIRCLE_SIZE, edgecolor='w'),
       autopct='%.2f%%',
       pctdistance=INNER_PCTDISTANCE)
ax.set_title('주요 국가별 중첩 파이 그래프', fontsize=16)
plt.show()


















