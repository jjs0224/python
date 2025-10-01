import numpy as np
import pandas as pd

data = {
    '이름':['철수','영희','민수','길동','미나','영수','수현','민지'],
    '학년':[1,1,2,2,3,3,2,1],
    '반':[1,1,1,2,2,3,2,3],
    '국어':[90,85,70,95,60,75,80,88],
    '영어':[88,92,75,80,65,70,85,98],
    '수학':[95,80,88,70,90,85,75,92]
}

df = pd.DataFrame(data)
print(df)
group1 = df.groupby('학년')
print(group1[['국어','영어','수학']].mean())

#2.반별 수학 최고점
group2 = df.groupby('반')
print(group2[['수학']].max())


#3.학년+반별 영어 평균
group3 = df.groupby(['학년','반'])
print(group3[['영어']].mean())


#4.학년별 집계
print(group1.agg({'국어':'mean','영어':'sum','수학':'max'}))

#5.학년별 학생수
print(group1[['학년']].value_counts())

#6.반별 평균 수학 점수 내림차순 정렬
mean_v = group2[['수학']].mean().sort_values(by='수학', ascending=False)
print(mean_v)

#7.transform: 학년별 국어 평균 초과 여부p
df['국어평균']=group1[['국어']].transform('mean')
df['평균초과여부']= df['국어']> df['국어평균']
print(df)

#8.학년별 영어 Top1 학생
idx = group1['영어'].idxmax()
max_s=df.loc[idx,['학년','이름','영어']].sort_values('학년')
print(max_s)

top_s = group1['영어'].max()
print()