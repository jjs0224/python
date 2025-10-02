class CustomRange:
    def __init__(self, stop):
        self.current = 0
        self.stop = stop

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.stop:
            rvalue = self.current
            self.current += 1
            return rvalue
        else:
            raise StopIteration
        
    def __getitem__(self, index):
        if index < self.stop:
            return index
        else:
            raise IndexError
        
# for i in CustomRange(5):
#     print(i)

x, y, z = [10, 20, 30]
print(x,y,z)

a, b, c = CustomRange(3)
print(a,b,c)

ld1 = [40,20,10]
print(ld1[1])
print(ld1.__getitem__(1))

cr1 = CustomRange(4)
print(cr1[2])
print(cr1[5])