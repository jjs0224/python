import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rc('font', family='Malgun Gothic')

# data = [5, 25, 50, 20]
# #data : 각 몇퍼센트인지 , 시계반대방향으로 지정해줌.. rotation=0 위치에서시작
# plt.pie(data)
# plt.show()

data = pd.read_csv('covid_data.csv', index_col='국가')
chartdata = data.loc[['독일','프랑스','중국','영국'], '4월06일']
print(chartdata)

mylabels = chartdata.index
#pie graph 에서 나중에 인덱스값그대로 사용가능
print(mylabels) #Index(['독일', '프랑스', '중국', '영국'],
mycolors = ['blue','#6aff00', 'yellow', '#ff113c'] #사용할 색 정해주기

def getLabelFormat(pct, allvalues):
    absolute = int(pct / 100 * np.sum(allvalues))
    return f'{pct:.2f}\n{absolute}명'

plt.figure(figsize=(8,8))
plt.pie(chartdata, #1차원 형식의 데이터만 들어감..NO DATAFRAME
        labels=mylabels,
        startangle=90,   #시작점을 바꿔주기
        colors=mycolors,
        autopct=lambda pct: getLabelFormat(pct, chartdata), #퍼센트별로 몇명인지도 표시하고싶을때
        textprops=dict(color='#bbbbbb', weight='bold', size=15),
        counterclock=False, #시계방항으로 데이터 표시
        explode=(0,0.1,0,0), #각데이터를 몇퍼센트 떼어놓을지 지정(두번째=프랑스를 떼어놓음)
        shadow=True, #그림자 표시
        )
plt.legend(title='국가명', title_fontsize=15, loc='best') #legend 표시
plt.title('주요 국가 코로나 발생 비율(4월6일)', fontsize=16)
plt.xlabel('<국가명>', fontsize=14)
plt.show()



















