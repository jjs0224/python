ldata1 = []
for i in range(10):
    ldata1.append(i)
print(ldata1) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print()

ldata2 = [i for i in range(10)] #위랑같은결과인데 이방법이 훨씬빠름
print(ldata2) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print()

ldata3 = []
for i in range(10):
    if(i % 2 == 0):
        ldata3.append(i)
print(ldata3) #[0, 2, 4, 6, 8]
print()

ldata4 = [i for i in range(10) if i % 2 == 0 ] #if 가 true 일때만 i 값전달함 =>짝수만들어가는 리스트 생성됨
print(ldata4) #[0, 2, 4, 6, 8]

ldata5 = []
for i in range(10):
    if(i % 2 == 0):
        ldata5.append(i)
    else:
        ldata5.append(100)
print(ldata5) #[0, 100, 2, 100, 4, 100, 6, 100, 8, 100]
print()

ldata6 = [i if i % 2 == 0 else 100 for i in range(10)] #else 까지 같이 사용할경우 무조건 앞에먼저 선언해줘야함
print(ldata6) #[0, 100, 2, 100, 4, 100, 6, 100, 8, 100]

print([i*j for i in range(2, 10) for j in range(1, 10)]) #[2, 4, 6, 8, 10, 12, 14, 16, 18, 3, 6, 9, 12, 15, 18, 21, 24, 27, 4, 8, 12, 16, 20, 24, 28, 32, 36, 5, 10, 15, 20, 25, 30, 35, 40, 45, 6, 12, 18, 24, 30, 36, 42, 48, 54, 7, 14, 21, 28, 35, 42, 49, 56, 63, 8, 16, 24, 32, 40, 48, 56, 64, 72, 9, 18, 27, 36, 45, 54, 63, 72, 81]

print(tuple(i for i in range(10))) #(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

data1 = [1,2,3,4,5]
data2 = [10,20,30,40,50]
data3 = [100,200,300,400,500]


result = [i+j+k for i,j,k in zip(data1, data2, data3) ] #앞에 코드들어가고 which values 는 (,) 이렇게 선언해줌
print(result)
print([sum(data) for data in zip(data1, data2, data3)]) #tuple 이면 sum() 을통해 안에있는 값들을 더해줄수있음 

