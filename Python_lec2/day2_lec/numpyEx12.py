import numpy as np

np.random.seed(12345)

arr = np.random.randn(5, 3)
print(arr)
print()
arr.sort(axis=1)
print(arr)
arr.sort(axis=0)
print(arr)

print(arr[::-1])

