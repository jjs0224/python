class Person2:
    def __init__(self):
        self.hello = 'good morning'
        self.name = 'kim'
        self.age = 20
        self.address = 'incheon'

    def greeting(self):
        print(f'{self.hello} I am {self.name} my address is {self.address}')

obj1 = Person2()
obj1.greeting() #good morning I am kim my address is incheon
print(obj1.name)