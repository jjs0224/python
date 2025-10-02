class Phone:  #Parent Class
    def call(self, number):
        print(number, '에게 전화를 겁니다.')
    
    def sendMessage(self, number, message):
        print(f'{number}에게 {message}을/를 보냅니다.')

phone = Phone() #Phone class 객체 생성
phone.call('010-7878-8989') #010-7878-8989 에게 전화를 겁니다.
phone.sendMessage('010-7878-8989', '좋은 하루입니다.') #010-7878-8989에게 좋은 하루입니다.을/를 보냅니다.  

class CM_Phone(Phone):  #Child Class(Parent Class)->이렇게 선언해주면 부모클라스사용가능
    def playMusic(self, title):
        print(title, '을/를 플레이합니다.')
    
    def takePicture(self):
        print('사진을 찍습니다.')

cm_phone = CM_Phone() #cm_phone 을사용해서 CM_Phone() 객체를 생성
cm_phone.playMusic('sky') #sky 을/를 플레이합니다.
cm_phone.takePicture() #사진을 찍습니다.
cm_phone.call('010-898-7878') #010-898-7878 에게 전화를 겁니다. (부모클라스 함수들사용가능)
cm_phone.sendMessage('010-8989-7878', 'hello') #010-8989-7878에게 hello을/를 보냅니다. (부모클라스 함수들사용가능)