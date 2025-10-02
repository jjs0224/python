class Person2:
    def __init__(self, insa, name, age, address):
        self.hello = insa
        self.name = name
        self.age = age
        self.address = address

    def greeting(self):
        print(f'{self.hello} I am {self.name} my address is {self.address}')
obj = Person2('hello', 'lee', 20, 'seoul')
obj.greeting() #hello I am lee my address is seoul

obj2 = Person2('good', 'choi', 40, 'busan')
obj2.greeting() #good I am choi my address is busan