class Person4:
    count = 0

    def __init__(self):
        Person4.count += 1 #class 자체의 count 값을 선언함 => 클라스 사용자가 다 공용으로쓸수있음

    @classmethod #공용으로 사용하기위한 클라스 자체의 메서드. (똑같은클라스많이만들 필요가없을경우 추천)
    def print_count(cls): #cls = class 자체주소값을 받아와서 따로 메모리에 print_count 를 저장함 (to be used for all objects using this class)
        print('{}의 객체가 생성되었습니다.'.format(cls.count))

james = Person4() #여기서 james 는 __init__ 만 생성해서 메모리에 저장함. classmethod 는 따로 저장됨
maria = Person4() #여기서 maria 는 __init__ 만 생성해서 메모리에 저장함. classmethod 는 따로 저장됨

Person4.print_count() #2의 객체가 생성되었습니다.
