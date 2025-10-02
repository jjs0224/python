# ldata1 = [10, 20, 30, 40]
# print(ldata1)

# ldata2 = ['choi', 3232.32, False]
# print(ldata2)
# ldata3 = [100, [80, 90], 'abc']
# print(ldata3) #[100, [80, 90], 'abc']
# print(len(ldata3)) #3

# ldata4 = [10, 20, 30]
# print(ldata4)
# ldata4.append(40) #.append => 리스트 맨뒤에 한개의 객체를 붙힘
# print(ldata4)            #[10, 20, 30, 40]
# ldata4.append([50, 60])
# print(ldata4)            #[10, 20, 30, 40, [50, 60]]

ldata5 = [10, 20, 30]
print(ldata5)
ldata5.extend([50, 60])  #list 들을 연결시켜줌 so extends list
print(ldata5)               #[10, 20, 30, 50, 60]
ldata5.extend(70)
#print(ldata5)               #TypeError: 'int' object is not iterable