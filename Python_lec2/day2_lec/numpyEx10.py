import numpy as np

np.random.seed(12345)
arr = np.random.rand(5,4)
print(arr)
print()

print(f'평균: {arr.mean()}')
print(f'평균: {np.mean(arr)}')

print(f'표준편차: {arr.std()}')
print(f'분산: {arr.var()}')
print(f'합: {arr.sum()}')
print()

print(f'열 평균: {arr.mean(axis=0)}' ) #각행들의 순번대로 평균값구한거 [:,0] [:,1] [:,2] [:,3]
print(f'행 평균: {arr.mean(axis=1)}') #각 열들의 평균을 구함(each row) [0,:] [1,:] [2,:] [3,:]
print()

arr2 = np.arange(10)
print(arr2)
print(arr2.cumsum())
print()

arr3 = np.array([[0,1,2],
                [3,4,5],
                [6,7,8]])
print(arr3)
print(f'열 누적함:\n{arr3.cumsum(axis=0)}')
print(f'열 누적곱:\n{arr3.cumprod(axis=0)}')
