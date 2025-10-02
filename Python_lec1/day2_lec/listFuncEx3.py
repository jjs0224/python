# ldata1 = [10, 20, 30, 40, 50]
# print(ldata1)
# ldata2 = ldata1
# print(ldata2)
# ldata2[1] = 2000
# print(ldata2)  #[10, 2000, 30, 40, 50]
# print(ldata1)  #[10, 2000, 30, 40, 50]

ldata3 = [10, 20, 30, 40, 50]
ldata4 = ldata3.copy()
ldata4[1] = 2000
print(ldata4)  #[10, 2000, 30, 40, 50]
print(ldata3)  #[10, 20, 30, 40, 50]

ldata5 = [10, 20, 30, 40, 50]
ldata6 = ldata5.copy()
print(ldata5 == ldata6)  #True  객체안에있는값을 비교함
print(ldata5 is ldata6)  #False  is 는 같은객체인지 주소를 비교함

