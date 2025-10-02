# class Person3:
#     def greeting(self):
#         print('hello')

# class Student(Person3):
#     def greeting(self): #부모랑 같은함수인데 여기서 overriding(재정) 해줌..그래서 결과는 이걸로찍힘
#         print('good morning')

# james = Student()
# james.greeting() #good morning

class Point2D:
    def __init__(self):
        self.x_point = 100
        self.y_point = 200

    def print_point(self):
        print('xPoint:', self.x_point)
        print('yPoint:', self.y_point)

class Point3D(Point2D):
    def __init__(self):
        super().__init__() #Parent class x_point & y_point 사용가능하게 선언해줌
        self.z_point = 300

    def print_point(self): 
        super().print_point() #Parent class 함수 접근가능하게 만들어줌(overriding 할수있음) !이름꼭같아야함!
        print('zPoint:', self.z_point)

p2 = Point2D()
p2.print_point()    #xPoint: 100
                    #yPoint: 200
p3 = Point3D()
p3.print_point()
                    #xPoint: 100
                    #yPoint: 200
                    #zPoint: 300