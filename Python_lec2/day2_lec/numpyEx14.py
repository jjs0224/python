import numpy as np

names = ['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe']
print(names)
print(np.unique(names))
print()

values = np.array(([6,0,0,3,2,5,6]))
print(values)
print(np.union1d(values, [2,3,6]))
print(np.intersect1d(values, [2,3,6]))
print(np.setdiff1d(values, [2,3,6,8]))
print(np.setxor1d(values, [2,3,6,8]))
print(np.isin(values, [2,3,6]))

