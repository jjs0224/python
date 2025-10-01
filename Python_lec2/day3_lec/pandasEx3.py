import pandas as pd
import numpy as np

obj1 = pd.Series([4,2,6,9], index = list('abcd'))
print(obj1)
print(obj1['b'])
print(obj1.iloc[1])

print(obj1.iloc[1:3])

print(obj1['b':'d']) #여기서 슬라이싱은 'd' 까지 포함됨 그래야 마지막껏도 불러올수있음



frame = pd.DataFrame(np.arange(16).reshape(4, 4),
                    index=['서울','부산','인천','대전'],
                     columns=['one','two','three','four'])
print(frame)
print()
print(frame.loc['부산']['one'])
print(frame.iloc[1, 0])
print(frame.iloc[2:, 2:])
print(frame.loc['인천':'대전','three':'four'])
print(frame.iloc[:, :3][frame.three>5])
print(frame.iloc[:,:3])
print(frame.three>5) #여기서 True 인것들만 가져옴=>부산,인천,대전

























