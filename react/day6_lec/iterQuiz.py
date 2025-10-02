class MultiIterator:
    def __init__(self, stop, multi):
        self.stop = stop
        self.multi = multi
        self.index = 1

    def __iter__(self):
        return self
    
    def __next__(self):
        value = self.index * self.multi
        if value < self.stop:
            self.index += 1
            return value
        else:
            raise StopIteration
        
user_input, multi = input('두 숫자를 입력하세요:').split()
for n in MultiIterator(int(user_input), int(multi)):
    print(n, end=' ')
