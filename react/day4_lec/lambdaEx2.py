ldata1 = [1,2,3,4,5,6,7,8,9,10]

ldata2 = list(map(lambda x : str(x) if x % 3 ==0 else x, ldata1))
print(ldata2) #[1, 2, '3', 4, 5, '6', 7, 8, '9', 10]

ldata3 = [1,2,3,4,5]
ldata4 = [2,4,6,8,10]

result = list(map(lambda x, y: x*y,  ldata3, ldata4)) #map 사용할때 x, y에 값을넣어서도 사용가능
print(result) #[2, 8, 18, 32, 50]

def f_func(x): #when function is called, get the value 
    return x > 5 and x < 10 #if this is true, return x , else x 버려

ldata5 = [8,3,2,9,1,7,4,5,6]
result = list(filter(f_func, ldata5)) #f_func 에서 리턴된값만 result 에 넣어줌
print(result) #[8, 9, 7, 6]

