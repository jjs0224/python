class SquareIteragor:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.numbers):
            value = self.numbers[self.index] ** 2
            self.index += 1
            return value
        else:
            raise StopIteration

user_input = input('제곱할 숫자들을 입력하세요: ') #제곱할 숫자들을 입력하세요: 3 2 4 5
nums = list(map(int, user_input.split()))

print('\n제곱 결과')
for n in SquareIteragor(nums): #
    print(n, end=' ') #9 4 16 25 