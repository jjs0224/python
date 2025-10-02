# ldata1 = [1.3, 2.3, 4.1, 8.2]
# for i in range(len(ldata1)):
#     ldata1[i] = int(ldata1[i])  #정수로만들어줌
# print(ldata1)   #[1, 2, 4, 8]

# ldata2 = [1.3, 2.3, 4.1, 8.1]

# print(list(map(int, ldata2))) #[1, 2, 4, 8] 
# print(list(map(str, ldata2))) #['1.3', '2.3', '4.1', '8.1']

# idata = input('두 정수를 입력하세요: ').split()
# print(idata)
# for i in range(len(idata)):
#     idata[i] = int(idata[i])
# print(idata)

# idata = list(map(int, idata))

num1, num2 = list(map(int, input('두 정수를 입력하세요').split())) #list 형태로 받아오기때문에 언패킹사용해서 num1, num2 바로 값 넣어줄수있음
print(num1+num2)

idata = input('이름 나이 주소를 입력하세요: ')
print(idata.split())

name, age, address = input('이름 나이 주소를 입력하세요: ').split()
print(name)
print(age)
print(address)