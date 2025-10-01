import pandas as pd
import numpy as np

print('----많은데이터 쪼개서 불러오고싶을때-----')
chunker= pd.read_csv('data/ex6.csv', chunksize=1000)#쪼갤양(1000)선언
print(chunker)
print()
for data in chunker: #for loop 사용해서 1000개씩 쪼개져있는 데이터 불러오기
    print(data)

print('-----각 밸류들이 몇개씩있는지 카운팅해줘서 리턴----')
sdata = pd.Series(['a','b','a','c','d','a','c'])
print(sdata)
print()
print(sdata.value_counts())

print('----많은데이터 쪼개서 불러오고싶을때-----')
chunker= pd.read_csv('data/ex6.csv', chunksize=1000)#쪼갤양(1000)선언

tot = pd.Series([], dtype=np.float64)
for piece in chunker: #for loop 사용해서 1000개씩 쪼개져있는 데이터 불러오기
    tot=tot.add(piece['key'].value_counts(),fill_value=0)

print(tot)
tot.sort_values(ascending=False, inplace=True)
print(tot[:10])
































