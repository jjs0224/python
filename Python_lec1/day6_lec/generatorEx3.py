def evenNum_generator(numbers):
    for num in numbers:
        if num % 2 == 0:
            yield num

numbers = list(map(int, input('정수들을 입력하세요: ').split()))

for number in evenNum_generator(numbers):
    print(number, end=" ")