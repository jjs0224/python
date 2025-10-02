import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

frame = pd.read_csv('tips.csv', index_col=0)
print(frame)
print(frame.time.unique()) #['Dinner' 'Lunch']

dinner = frame.loc[frame['time'] == 'Dinner', 'total_bill']
dinner.index.name = 'Dinner'
print(dinner) #Dinner 의 total_bill 값만 가져옴

lunch = frame.loc[frame['time'] == 'Lunch', 'total_bill']
lunch.index.name = 'Lunch'
print(lunch) #lunch 의 total_bill 만 가져옴

#figure size 랑 각 axes객채 받을수있음.. 여기서 1row, 2col 선언해줬음으로..
#figure size 가 두column 으로나뉘고 axes = [<Axes: > <Axes: >]
#이거를 언패킹해서 받아도됨..=> fig, (ax1, ax2) 이런식으로 ...
fig, axes = plt.subplots(1,2,figsize=(11,6))
print(axes)

#첫번째 그래프 설정-boxplot, vert
axes[0].boxplot(dinner, vert=True)
axes[0].set_title('vertical boxplot(dinner_total_bill)')
#두번째 그래프 설정-boxplot, vert
axes[1].boxplot(lunch, vert=True)
axes[1].set_title('vertical boxplot(lunch_total_bill)')

plt.show()










