import numpy as np

arr = np.arange(10)
print(arr)
print(np.exp(arr))
print(np.square(arr))
print(np.sqrt(arr))
print()

print(np.sin(arr))
print(np.cos(arr))
print()

x = np.array([5,2,8,6,11,6,99])
y = np.array([1,2,3,4,5,66,77])
print(np.maximum(x, y))
print(np.minimum(x, y))

arr2 = np.array([32.62, 5.09, 0.321, 954.98])
data = np.modf(arr2) #소수점이랑 그위수들을 나눠줌
print(data)
print(data[0]) #소수점들 (decimal point 모아둔어레이)
print(data[1]) #소수점위에 (real number 모아둔어레이)