import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
plt.rc('font', family='Malgun Gothic')

data = pd.read_excel('fine_dust.xlsx', index_col = 'area')
#index_col= column 을 인덱스로 쓰고싶을때 그 콜롬을 index_col 로지정해주기
print(data)

data2018 = data[2018]
print(data2018)
#
# plt.figure(figsize=(15,4))
# plt.title('2018 data')
# plt.plot(data2018, color='lightblue', marker='o')
# plt.xlabel('area')
# plt.ylabel('2018 fine dust line graph')
# plt.grid(True)
# plt.show()

plt.figure(figsize=(15,4))

for year in range(2016, 2020):
    chartData = data[year]
    plt.plot(chartData, marker='s', label=year)

plt.xlabel('area/지역')
plt.ylabel('micrometer')
plt.title('2016 - 2019 fine dust line graph')
plt.legend(loc='best')
plt.grid(True)
plt.show()






























