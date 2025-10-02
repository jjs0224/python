# endValue = int(input('정수 값을 입력하세요:'))

# result = 0
# i=1

# while i <= endValue:
#     result += i
#     i += 1

# print(endValue, '까지의 합은', result, '입니다')
# result = 0
# i = 1
# while True:
#     result += i
#     if(result > 1000):
#         break
#     i += 1

# print('누적값이 1000을 넘었을때의 i 값: ', i)

i = 0
result = 0

while i < 100:
    i += 1
    if i % 2 == 0:
        result += i
        continue
        
    print(i)

print('누적값', result)