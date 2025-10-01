import numpy as np

ldata1 = [10, 20, 30, 40]
print(ldata1) #[10, 20, 30, 40]
print(type(ldata1)) #<class 'list'>
print()

arr1 = np.array(ldata1)
print(arr1) #[10 20 30 40]
print(type(arr1)) #<class 'numpy.ndarray'>
print()

ldata2 = [[1,2,3,4], [5,6,7,8]]
print(ldata2) #[[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(ldata2)
print(arr2)
print(arr2.shape) #(2, 4)
print(arr2.dtype) #int64
print()

ldata3 = [10.4, 23, 5233.12, 11]
print(ldata3) #[10.4, 23, 5233.12, 11]
arr3 = np.array(ldata3, dtype=np.int32)
print(arr3) #[  10.4    23.   5233.12   11.  ]
print(arr3.dtype) #float64

ldata4 = ['1.23', 33.23, 431]
print(ldata4)
arr4 = np.array(ldata4) #어레이로 바꿀때 dtype= 값을 지정안해주면 제일큰값으로 정해준다 int<float<string
print(arr4) #['1.23' '33.23' '431']
arr5 = np.array(ldata4, dtype=np.float64) #dtype 을 플로트로 정해줌
print(arr5) #[  1.23  33.23 431.  ]
