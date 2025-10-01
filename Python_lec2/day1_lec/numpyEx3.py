ldata1 = [10, 20, 30, 40]
ldata2 = [100, 200, 300, 400]
ldata3 = ldata1 + ldata2
print(ldata3)

import numpy as np

arr1 = np.array(ldata1)
arr2 = np.array(ldata2)
arr3 = arr1 + arr2 #shape (len(arr1) and len(arr2) 가 같아야함!!!!!)
print(arr3)
print()

arr4 = np.array([[10, 20, 30],
                 [40, 50, 60]])
arr5 = np.array([[1, 2, 3],
                 [5, 6, 7]])

print(arr4 + arr5)
print()
print(arr4 - arr5)
print()
print(arr4 * 10)
print()
print(1/arr4)
print()

arr5 = np.array([100, 200, 300])
print(arr4)
print(arr5)
print()
print(arr4 + arr5)

arr6 = np.array([[3,2,8],
                 [0,3,7]])
arr7 = np.array([[9,1,7],
                 [2,2,9]])
print(arr6)
print()
print(arr7)
print()
print(arr6 > arr7)
print()
print(arr7 > 5) #each value in arr7, 5보다 큰지 비교