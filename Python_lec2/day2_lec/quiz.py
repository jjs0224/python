import numpy as np

xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])

result = [x if z else y for x, y, z in zip(xarr, yarr, cond)]
print(result)
print()

result2 = np.where(cond, xarr, yarr) #condition 이 True => 첫번째(xarr),  false => 두번째(yarr)값을 가져온다
print(result2)

np.random.seed(12345)
arr = np.random.rand(4, 4)
print(arr)
print()

print(np.where(arr>0, 2, -2)) #arr>0 ,0보다크면 2를, 0보다 작으면 -2를 리턴
print(np.where(arr>0, 2, arr)) #arr>0, 0보다 크면 2를, 0보다 작으면 어레이값을 가져옴
print()

data = np.array([3,2,5,7,8,7,3,7])
print(np.where(data == 7)) #7값을 가진 인덱스값을 리턴