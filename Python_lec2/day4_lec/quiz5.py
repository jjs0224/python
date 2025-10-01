#join outer
#최종점수 = 중간고사 만약에없으면 기말고사
#둘다없으면 나머지점수의 평균값(수현)
#등급으로나눔

import pandas as pd
import numpy as np

data1 = pd.read_csv('data/final.csv')
data2 = pd.read_csv('data/midterm.csv')
print(data1)
print(data2)
frame = pd.merge(data2,data1, how='outer' )
print(frame)

frame['최종점수']=frame['중간고사'].combine_first(frame['기말고사'])
print(frame)

mean_ = frame['최종점수'].mean(skipna=True)
frame['최종점수']=frame['최종점수'].fillna(mean_)
print(frame)

grade = [0,69,79,89,100]
labels=['D','C','B','A']
frame['학점']=pd.cut(frame['최종점수'], bins=grade, labels=labels,include_lowest=True)

print(frame)

