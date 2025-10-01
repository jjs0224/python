import numpy as np
import pandas as pd

frame = pd.DataFrame(np.random.randn(4,3),
                     columns=['서울','부산','인천'],
                     index=['김가','이가','최가','오가'])
print(frame)

print( frame['서울'].max()-  frame['서울'].min())
print( frame['부산'].max()-  frame['부산'].min())
print( frame['인천'].max()-  frame['인천'].min())

f1 = lambda x : x.max() - x.min()
result1 = frame.apply(f1, axis=0)
print(result1)

f1 = lambda x : x.max() - x.min()
result1 = frame.apply(f1, axis=1)
print(result1)
print()

def f2(x):
    return pd.Series([x.mean(), x.std()],index=['mean','std'])

result2 = frame.apply(f2, axis=0)
print(result2)

f3 = lambda x: f'{x:.2f}' #소수점2자리형태로 만들어줄 함수
result3 = frame.map(f3) #모든값에 f3 함수 적용함
print(result3)
print()

sd = frame['인천']
print(sd)

print(sd.map(f3))
print(sd.apply(f3))
