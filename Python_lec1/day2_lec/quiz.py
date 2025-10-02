type1 = []
inputv = input('join <이름> / leave / show / exit: ').split()

while inputv[0] != 'exit':

    if(inputv[0]!='join' and inputv[0]!='exit' and inputv[0]!='leave' and inputv[0]!='show'):
        print('잘못된 명령어입니다')

    if(inputv[0]=='join' and len(inputv)==1):
        print('제대로된 사용법: join을 입력하고 이름을 입력하세요')

    if len(inputv) == 2:

        name = inputv.pop()
        type1.append(name)
        print(type1)

    if(inputv[0]=='leave'):
        if(len(type1)!=0):
            person = type1.pop(0)
            print(person, '나갔습니다')
        else:
            print('더이상 이름이 없습니다')     

    if(inputv[0] == 'show'):
        print(type1)

    inputv = input('join <이름> / leave / show / exit: ').split()

print('프로그램종료!')


