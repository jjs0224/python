ldata1 = ['kim', 'lee', 'choi', 'oh']
print(ldata1)

print(ldata1[0])
print(ldata1[1])
print(ldata1[2])
print(ldata1[3])
# print(ldata1[4]) //indexTypeError-out of range error

print()
print(ldata1[3])
print(ldata1[-1]) #oh
print(ldata1[-2]) #choi
print(ldata1[-3]) #lee
print(ldata1[-4]) #kim
print()

ldata2 = ['seoul', 'busan', 'incheon', 'dagu', 'suwon', 'gangju', 'jinju']
print(ldata2)
print(ldata2[1:4]) # 1 =< x < 4  #['busan', 'incheon', 'dagu']
print(ldata2[:5]) # ['seoul', 'busan', 'incheon', 'dagu', 'suwon'] from 0->5
print(ldata2[2:]) # ['incheon', 'dagu', 'suwon', 'gangju', 'jinju'] 2->end
print(ldata2[:]) # ['seoul', 'busan', 'incheon', 'dagu', 'suwon', 'gangju', 'jinju']

print(ldata2[-3:]) #['suwon', 'gangju', 'jinju'] //편하게 마지막3개 불러올수있음

print(ldata2)
print(ldata2[1:6]) #['busan', 'incheon', 'dagu', 'suwon', 'gangju']
print(ldata2[1:6:2]) #['busan', 'dagu', 'gangju'] ++2
print(ldata2[::2]) #['seoul', 'incheon', 'suwon', 'jinju']
print(ldata2[::-1]) #['jinju', 'gangju', 'suwon', 'dagu', 'incheon', 'busan', 'seoul'] //여기서 -는 역순위
print(ldata2[::-2]) #['jinju', 'suwon', 'incheon', 'seoul'] 역순위로 every second item 불러오기

ldata3 = ['red', 'blue', 'green']
print(ldata3) #['red', 'blue', 'green']
ldata3[1] = 'pink'
print(ldata3) #['red', 'pink', 'green']

