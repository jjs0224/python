import numpy as np
import pandas as pd

np.random.seed(12345)

frame = pd.DataFrame(np.random.randn(5,5),
                     index=['joe','steve','wes','jim','travis'],
                     columns=list('abcde'))

print(frame)
print()
mapping = {'a':'red', 'b':'red', 'c':'blue','d':'blue','e':'red'}
grouped1 = frame.groupby(mapping, axis=1)
print(grouped1.sum())
print()

print('===인덱스를 라벨링해주고 그거대로 groupby 해주기===')
labeling = ['one','one','one','two','two'] #joe=one, steve=one...이렇게 레이블 달아줌
grouped2 = frame.groupby(labeling)
print(grouped2.mean())
print()

print('===글자수 length로 라벨링해주고 groupby 로 나눠주기===')
#joe=3, steve=5, wes=3, jim=3, travis=5
grouped3 = frame.groupby(len)
print(grouped3.sum())

grouped4 = frame.groupby(lambda x : x[-1])
print(grouped4.mean())

print(frame.groupby([len, labeling]).min())