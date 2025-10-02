import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

plt.rc('font', family='Malgun Gothic')

welfare = pd.read_csv('welfareClean.csv', encoding='cp949')
# print(welfare)
# welfare.info()
# print(welfare.tail(10))

# result = welfare.groupby('결혼 유무')['결혼 유무'].count()
# print(result)
#
# plt.bar(result.index, result.values)
# plt.show()
#결혼유무 바그래프 그리기 order=[] 통해 순서정해주기
#sns.countplot(data=welfare, x='결혼 유무', order=['결혼','이혼','무응답'])
#결혼유무 중 종교도 포함시켜주기
#sns.countplot(data=welfare, x='결혼 유무', order=['결혼','이혼','무응답'],hue='종교 유무')
#결혼유무 중 종교유무 도 그려주기, palette= 사용해서 색상정해주기
# sns.countplot(data=welfare, x='결혼 유무', order=['결혼','이혼','무응답'],hue='종교 유무',palette='Paired')
# plt.title('count plot', fontsize=18)
# plt.show()

# pdata = welfare.pivot_table(index='성별',
#                             columns='결혼 유무',
#                             values='나이',
#                             aggfunc='mean')
# print(pdata)
# #색상그래프 (annot=True) => 안에 값 표시해주기
# # sns.heatmap(data=pdata, annot=True)
# # plt.show()
#
# corr = welfare[['생일','소득','나이']].corr()
# print(corr)
# #cmap= color map 바로사용가능
# sns.heatmap(data=corr, annot=True, cmap='YlGnBu')
# plt.show()

# nwelfare = welfare.loc[:, ['생일','소득','나이','결혼 유무']]
# print(nwelfare)
# sns.pairplot(data=nwelfare, hue='결혼 유무')
# plt.show()

# sns.violinplot(x='성별', y='나이', data=welfare, hue='종교 유무')
# plt.show()

sns.lmplot(x='나이',y='소득',data=welfare, hue='결혼 유무',
           col='성별', row='연령대')
plt.show()













