import pandas as pd
import numpy as np

obj1 = pd.Series([4,7,-5,3], index=list('dabc'))
print(obj1)
print()

obj2 = obj1.reindex(list('abcde'))
print(obj2) #Nan 은 float 이기때문에 float 로 데이터타입이바뀜

obj3 = pd.Series(['blue','purple','yellow'], index = [0,2,4])
print(obj3)

obj4 = obj3.reindex(np.arange(6))
print(obj4)

obj5 = obj3.reindex(np.arange(6), method='ffill') #ffill=frontfill(앞에값으로채움)
print(obj5)
print()

frame = pd.DataFrame(np.arange(9).reshape(3,3),
                     index=list('acd'),
                     columns=['ohio','texas','california'])
print(frame)
print()
print(frame.reindex(index=list('abcd')))
print(frame.reindex(columns=['texas','utah','california']))
print(frame.reindex(index=list('abcd'), columns=['texas','utah','california']))