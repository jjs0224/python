class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print('....')

    def info(self):
        print(f'나는 {self.name}입니다')

class Dog(Animal):
    def speak(self): #overriding parent class method speak()
        print('멍멍~~~')

class Cat(Animal):
    def speak(self): #overriding parent class method speak()
        print('야옹~~~')

dog = Dog('바둑이')
cat = Cat('토리')

dog.info()  #나는 바둑이입니다
cat.info()  #나는 토리입니다
dog.speak() #멍멍~~~
cat.speak() #야옹~~~