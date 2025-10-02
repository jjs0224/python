ldata = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
# print(ldata)  #[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
# ldata[2:5] = ['a']
# print(ldata)  #[0, 10, 'a', 50, 60, 70, 80, 90]  우리가 지정해준 range 안에포함하는 모든걸 'a' 로 체인지 //not change every index value with a but the whole block
# ldata[2:5] = 'a' #[0, 10, 'a', 50, 60, 70, 80, 90] 위에랑 결과는 같음

# ldata[2:5] = ['a', 'b', 'c', 'd', 'e']
# print(ldata)  #[0, 10, 'a', 'b', 'c', 'd', 'e', 90]

ldata[2:8:2] = ['a', 'b', 'c']
print(ldata) #[0, 10, 'a', 30, 'b', 50, 'c', 70, 80, 90]
