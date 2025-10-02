
nums = input('숫자들을 입력하세요:').split()
num = map(int,nums)

calc1 = list(map(lambda x : x * x, num))

even = list(filter(lambda x: x%2==0,calc1)) #true 일때 x 값돌릴때는 FILTER
print(even)



#각 값을 제곱해줌 -lambda
#짝수만 필터링
