import pandas as pd
import numpy as np

obj1 = pd.Series([4,7,-5,3])
print(obj1)
print(type(obj1))
#print()
print(obj1.index)
print(obj1.values)
print(type(obj1.values))
#print()

obj2 = pd.Series([4,7,-5,3], index=['a', 'b', 'c', 'a'])
print(obj2)
print(obj2['c']) #'c' 인덱스 가져오기
print(obj2[['c', 'b']]) #c 랑 b 인덱스위치에있는 값 불러오기
#print()
obj2['c'] = 100 #'c'인덱스 위치에있는 값 바꾸기
print(obj2)
#print()

print(obj2 *3) #모든값에 3 곱홰주기
#print()

print(obj2 > 5) #인덱스는 같고 값만 True or False
#print()
print(obj2[obj2 > 5]) #5보다 큰 값만 표시하기
#print()
print(np.exp(obj2))

ddata = {'ohio':35000, 'texas':72000, 'oregon': 18000, 'utah': 5000}
print(ddata)
print()
print()
obj3 = pd.Series(ddata) #딕셔너리를 시리즈로만들기(key=>index)
print(obj3)