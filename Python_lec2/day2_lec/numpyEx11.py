import numpy as np

np.random.seed(12345)

arr = np.random.randn(100)
print((arr>0).sum())
print()

bools = np.array([[False, False, True, False],
                  [False, False, True, True]])
print(bools.sum())
print()
print(bools.any()) #하나라도 트루이면 True. 모두 false 여야지 False
print(bools.any(axis=1))
print(bools.any(axis=0))
print(bools.all(axis=0)) #all 은 전부 True 일때만 True

data = np.random.randn(10, 4) *4
print(data)

print()
print(data[(data > 3).any(axis=1)])
print((data > 5).any(axis=0))
print(data[:, (data>5).any(axis=0)])
data1 = np.random.randn(10, 4) *4

