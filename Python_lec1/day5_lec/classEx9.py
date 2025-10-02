class Person:
    def greeting(self):
        print('hello~~~~')

class Student(Person):
    def study(self):
        print('studying~~~')

obj1 = Student()
obj1.study() #studying~~~
obj1.greeting() #hello~~~~