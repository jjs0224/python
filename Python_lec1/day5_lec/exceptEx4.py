class NotThreeMultipleError(Exception):
    def __init__(self, evalue): #2.evalue 따로 함수만들어줄때 여기도 포함시켜줌
        super().__init__('3의 배수가 아님!!!!!!') #1.에러자체 클라스에서 에러 값을 등록
        self.evalue = evalue #2.evalue 아얘 만들어줌

    def err_info(self): #2. 에러값 저장해줄 정보를 따로만들어줌
        print(f'에러를 발생시킨 값:{self.evalue}') #에러생성됬을때 어떤에러인지 출력해줄코드

def three_multiple():
    try:
        x = int(input('3의 배수를 입력하세요: '))
        if x % 3 != 0:
            raise NotThreeMultipleError() #1.클라스객체불러올때 메세지자동으로 선언됨(defined in __init__)
        print('입력 값:', x)
    
    except NotThreeMultipleError as e:
        print('예외 발생 : ', e) 
        e.err_info #2.어떤에러인지 err_info 함수통해 출력

three_multiple()