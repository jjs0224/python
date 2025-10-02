class Person2:
    def __init__(self):
        print('Person2.__init__()')
        self.name = 'kim'

class Student(Person2):
    def __init__(self):
        super().__init__() #Parent Class 변수에 접근가능 이거없으면 self.name 없다고 에러뜸!!!!
        print('Student.__init__()')
        self.message = 'hello~~~~'

    def print_info(self):
        print(f'{self.name}이/가 {self.message}라고 말합니다')

obj1 = Student()
obj1.print_info()
#--TERMINAL--
# Person2.__init__()
# Student.__init__()
# kim이/가 hello~~~~라고 말합니다

