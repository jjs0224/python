import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.pyplot import ylabel
plt.rc('font', family='Malgun Gothic')

data = pd.read_csv('covid_data.csv', index_col='국가')
chartdata = data['4월06일']
print(chartdata)

def makeBarChart1(x, y, colors, xlabel, ylabel, title):
    plt.figure(figsize=(11,8))
    plt.bar(x,y,color=colors, alpha=0.7)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)

    #y tick 구해서 지정해주기
    YTICK_INTERVAL = 50000
    maxlim = (int(y.max() / YTICK_INTERVAL) + 1) * YTICK_INTERVAL
    values = np.arange(0, maxlim + 1, YTICK_INTERVAL)
    print(values) #[     0  50000 100000 150000 200000 250000 300000 350000]
    plt.yticks(values, ['%s'%format(val, ',') for val in values])

    #각 국가별 ratio 구해서 bar 안에 text 로 넣어주기
    ratio = 100 * y / y.sum()
    print(ratio)
    for idx in range(y.size):
        #bar 중간에 몇퍼센트인지 ratio 표시해주기
        ratioVal = f'{ratio[idx]:.1f}%'
        plt.text(x=idx, y=y[idx]/2, s=ratioVal, ha='center', fontsize=9)

        #bar 맨위에 각 건 수 표시해주기
        value = format(y[idx], ',') + '건'
        plt.text(x=idx, y=y[idx]+2000, s=value, ha='center', fontsize=9)

        #평균 구해서 빨간줄로 표시해주기 + 평균값 .text 로 표시해주기
        meanval = y.mean() #평균값
        meantext = f'평균:{int(meanval)}건'
        plt.axhline(y=meanval, color='r', linewidth=1, linestyle='--')
        plt.text(x=y.size-1, y=meanval+3000, s=meantext, ha='center', fontsize=12)
    plt.show()

colors = ['b', 'g','r','c','m','y','k']
makeBarChart1(x=chartdata.index, y=chartdata, colors=colors,
              xlabel='국가명', ylabel='발생 수', title='국가별 코로나 발생 건 수(4월6일')