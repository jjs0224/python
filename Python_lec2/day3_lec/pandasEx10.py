import numpy as np
import pandas as pd

# obj1 = pd.Series(np.arange(4), index=list('dabc'))
# print(obj1)
# print()
# print(obj1.sort_index())
# print()
#
# frame1 = pd.DataFrame(np.arange(8).reshape(2,4),
#                       index=['three','one'],
#                       columns=list('dabc'))
# print(frame1)
# print(frame1.sort_index()) #row sorting
#
# print(frame1.sort_index(axis=1)) #column sorting
# print()
# print(frame1.sort_index(axis=1, ascending=False))

obj2 = pd.Series([4,7,-5,3])
print(obj2)
print()
print(obj2.sort_values())
print()

data = {'second': [4,7,-3,2], 'first':[0,1,0,1]}
frame2 = pd.DataFrame(data)
print(frame2)
print()
print(frame2.sort_values(by='second'))
print()
print(frame2.sort_values(by='first'))
print()
print(frame2.sort_values(by=['first','second'])) #first 기준으로 소팅하고 같은값이있을경우 세컨드도 소팅해줘라
print()
print(frame2.sort_values(by=['first','second'],ascending=[False, True])) #'first'는 내림차순, 'second'는 오름차순으로 지정