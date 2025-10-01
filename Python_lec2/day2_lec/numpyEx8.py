import numpy as np

arr = np.arange(8)
print(arr)
print()

arr2 = arr.reshape([4,2])
print(arr2)
print()

print(arr2.T) #T = trans  행과 열을 바꿔줌
print()

ldata = [10, 20, 30, 40, 50, 60]
arr3 = np.reshape(ldata, [3,2])
print(arr3)




