import numpy as np

arr1 = np.arange(0, 10, 1)
print(arr1) #[0 1 2 3 4 5 6 7 8 9]
print(type(arr1)) #<class 'numpy.ndarray'>
print()

arr1 = np.arange(0, 10)
print(arr1) #[0 1 2 3 4 5 6 7 8 9]
print(type(arr1)) #<class 'numpy.ndarray'>
print()

arr1 = np.arange(10)
print(arr1) #[0 1 2 3 4 5 6 7 8 9]
print(type(arr1)) #<class 'numpy.ndarray'>
print()

arr4 = np.linspace(-3, 3, 5) #-3에서 시작해서 3까지 5개의숫자를 배열해줌
print(arr4) #[-3.  -1.5  0.   1.5  3. ]
print(type(arr4)) #<class 'numpy.ndarray'>
print()

arr5 = np.ones([3,4]) # 튜플도가능함 np.ones((3,4))
print(arr5)
print()

arr6 = np.zeros([3,4]) #default 를 0 으로잡고 생성해줌
print(arr6)
print()

arr7 = np.empty([3,4]) #기존에 할당되어있는걸 가져옴.. arr6 위에 만들어둔걸 주석처리하면 arr5로 만들어둔걸 가져와서 사용하는거 비추천!!
print(arr6)
print()

arr8 = np.full([2,3], 100) #shape 랑 default 값까지 지정해주고싶을때
print(arr8)
print()

arr9 = np.ones_like(arr8) #arr8 을 본따서 SHAPE 따라함 근데 default 값은 1
print(arr9)
print()

arr10 = np.zeros_like(arr8)
print(arr10)
print()

arr11 = np.full_like(arr8, 50)
print(arr11)
