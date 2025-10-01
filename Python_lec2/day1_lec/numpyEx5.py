import numpy as np

arr1 = np.array([[1,2,7],
                 [6,7,9]])
print(arr1)
print()

barr1 = np.array([[True, False, True],
                  [False, False, True]])
print(barr1)
print(arr1[barr1]) #True 위치에 해당하는값만 가져옴
print()

barr2 = np.array([False, True])
print(barr2)
print(arr1[barr2])
print()

barr3 = np.array([True, False, True])
print(barr3)
print(arr1[:, barr3])

print()
