import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
plt.rc('font', family='Malgun Gothic')
data = pd.read_csv('students_scores.csv')
print(data)

fig = plt.figure(figsize=(10,6))
grid = plt.GridSpec(2,2,
                    width_ratios=[1,1], height_ratios=[1,1.3],
                    hspace=0.4)


data1 = data.groupby('학년')['수학'].apply(list)
data2 = data.groupby('학년')['영어'].apply(list)

data1_m = data.groupby('학년')['수학'].mean()
data2_m = data.groupby('학년')['영어'].mean()

colors = ['lightblue','lightgreen','lightpink']

ax1 = fig.add_subplot(grid[0])
ax1.set_title('학년별 수학 점수')

box = ax1.boxplot(data1.values, labels=['1학년','2학년','3학년'],
                  showmeans=True, patch_artist=True)
ax2 = fig.add_subplot(grid[1])
ax2.set_title('학년별 영어 점수')
box2 = ax2.boxplot(data2.values, labels=['1학년','2학년','3학년'],
                  showmeans=True, patch_artist=True)
years = data['학년'].unique()
year_index = range(len(years))
ax3 = fig.add_subplot(grid[-1,:])
ax3.set_title('학년별 평균 수학 & 영어 점수')
ax3.bar(data1_m.index-.15, data1_m, color=colors, width=0.3, alpha=0.7)
ax3.bar(data1_m.index+.15, data2_m, color=colors, width=0.3,edgecolor='k')
ax3.set_xticks(data1_m.index, ['1학년','2학년','3학년'])

for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

for patch, color in zip(box2['boxes'], colors):
    patch.set_facecolor(color)
plt.show()