import numpy as np
import pandas as pd

data = pd.Series([1, np.nan, 3.5, np.nan, 7])
print(data)
print()
print(data.dropna()) #na 값 다 drop 함
print()
print(data.notnull()) #null 이 아닌값은 True 를 리턴함
print(data[data.notnull()]) #null 이 아닌값을 데이터로 가져옴
print(data.isnull()) #null 인값을 True 로 리턴함
print()

np.random.seed(12345)
frame = pd.DataFrame(np.random.randn(7,3),
                     columns = ['seoul','busan','incheon'])
frame.iloc[:4, 1] = np.nan
frame.iloc[:2, 2] = np.nan
print(frame)

print(frame.fillna(0)) #na 를 전부 0으로 바꿔줌
print()
print(frame.fillna({'busan':-5, 'incheon':0})) #busan null 은 -5로채워주고, incheon null은 0으로채워줌
print(frame.fillna(pd.Series([-5, 0], index=['busan','incheon'])))
print()
print(frame.mean())
print()
print(frame.fillna(frame.mean()))
print()
print(frame.bfill())


data = {'one':np.arange(6),
        'two':np.arange(6,0,-1),
        'three':[1,1,1,2,2,2],
        'four':[0,1,2,0,1,2]}
frame2 = pd.DataFrame(data)
print(frame2)

print()
print(frame2.set_index('three')) #다른 column 을 인덱스로 지정해주기
print()
print(frame2.set_index(['two','four']))






















