import numpy as np
import pandas as pd

s1 = pd.Series([0,1], index=list('ab'))
s2 = pd.Series([2,3,4], index=list('cde'))
s3 = pd.Series([5,6], index=list('fg'))

print(s1)
print()
print(s2)
print()
print(s3)
print()

print(pd.concat([s1,s2,s3], axis=0))
print(pd.concat([s1,s2,s3], axis=1))
print()
print('----한 행에는 5 곱한수결과값이랑 s3 더해주기(vertical join)----')
s4 = pd.concat([s1 * 5, s3])
print(s4)
print()
print('----concat 사용해서 조인할경우 default 가 OUTERJOIN 이여서 NAN 값도포함해서 조인됨----')
print(pd.concat([s1,s4], axis=1))
print()
print('----Nan value 제외하고 조인하고싶을때 : INNERJOIN 선언해주기----')
print(pd.concat([s1,s4], axis=1, join='inner'))
print()

df1 = pd.DataFrame(np.arange(6).reshape(3,2),
                   index=list('abc'),
                   columns=['one','two'])
df2 = pd.DataFrame(np.arange(4).reshape(2,2),
                   index=list('ac'),
                   columns=['three','four'])
print(df1)
print()
print(df2)
print()
print(pd.concat([df1,df2], axis=1))
print()
print('----해당되는데이터별로 키 이름 정해주기(위에 한row 더생김)----')
print(pd.concat([df1,df2], axis=1, keys=['data1','data2']))