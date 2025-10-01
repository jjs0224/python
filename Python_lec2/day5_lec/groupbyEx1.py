import numpy as np
import pandas as pd

df = pd.DataFrame({'key1':['a','a','b','b','a'],
                   'key2':['one','two','one','two','one'],
                   'data1':np.random.randn(5),
                   'data2':np.random.randn(5)})
print(df)
print()


grouped1 = df.groupby('key1')
print(grouped1)
print()

print('====key1으로 묶어서 그룹해주기====')
for gd in grouped1:
    print(gd, end='\n\n')
print()

for gname, gdata in grouped1:
    print(gname)
    print(gdata)
print('===data1, data2 평균값구하기===')
print(grouped1[['data1','data2']].mean())
print('sum')
print(grouped1[['data2']].sum())
print()

print(list(grouped1))
print()
print(list(grouped1)[0][1])
print()

dcdata = dict(list(grouped1))
print(dcdata)
print()

print(dcdata['b'])

grouped2 = df.groupby(['key1','key2'])
for gd in grouped2:
    print(gd, end='\n\n')
print()

print(grouped2[['data1','data2']].sum())