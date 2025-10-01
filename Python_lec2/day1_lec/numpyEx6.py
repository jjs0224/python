import numpy as np

np.random.seed(12345)
data = np.random.randn(7, 4)
print(data)

# names = np.array(['bob', 'joe', 'will', 'bob', 'will', 'joe', 'joe'])
# print(names)
# print()
# print(names == 'bob')
# print()
# print(data[names == 'bob'])
# print()
# print(data[names == 'bob', 2:])
# print()
# print(data[names == 'bob', 3])
# print()


print(data < 0)
print()
print(data[data<0])

data[data < 0] = 0
print(data)

