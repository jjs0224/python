class Student:

    count = 0
    students = []

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        Student.count += 1
        Student.students.append(self) #객체로 넘겨줌

    def info(self):
        return f'{self.name} - {self.grade}학년'
    
    @classmethod
    def total_students(cls):
        return cls.count
    
    @classmethod
    def show_all(cls):
        for s in cls.students:
            print(s.info())

    @staticmethod
    def is_passing(score):
        return score >= 60 #return TRUE if it is true 
    
s1 = Student('kim', 2)
s2 = Student('lee', 1)
s3 = Student('hyo', 3)

print(s1.info())

print('전체 학생 수:', Student.total_students())
print('학생 목록:')
Student.show_all()

print('점수 75 합격여부:', Student.is_passing(75)) #점수 75 합격여부: True

