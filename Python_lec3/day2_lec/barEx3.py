import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.rc('font', family='Malgun Gothic')

data = pd.read_csv('covid_data.csv', index_col='국가')
datachart = data.loc[['프랑스','중국','영국','이란'], '4월06일':'4월08일']
print(datachart)

#-------dataFrame 자체로 그래프 그려줄수도 있음 ------
#-kind = 그래프 모양 정해주기
#-legend 는 디폴트로 포함됨
#-stacked 방식으로도 표현가능
datachart.plot(kind='bar', rot=0, title='국가별 일별 발생 수', legend=False, stacked=True)
plt.show()