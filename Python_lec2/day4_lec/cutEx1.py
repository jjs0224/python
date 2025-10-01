import pandas as pd

ages = [20, 22, 25, 27, 21, 37, 31, 62, 45, 41, 70, 32]
bins = [18, 25, 35, 60, 100]
print('-- (18,25]<= 18미포함, 25 포함사이에 있음...이걸 ages 안에있는 모든값으로 해줌--')
cdata = pd.cut(ages, bins)
print(cdata)
print(cdata.value_counts())
print()
cdata = pd.cut(ages,bins,right=False)
print(cdata)
print(cdata.value_counts())
print()
cdata = pd.cut(ages,bins,right=False,labels=['Youth','YoungAdult','MiddleAged','Senior'])
print(cdata)
print(cdata.value_counts())