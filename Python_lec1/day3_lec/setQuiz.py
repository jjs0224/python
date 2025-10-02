inputA = input('이름 입력(exit 입력 시 종료):')

classA = set()
classB = set()

while True:
    classA.update({inputA})
    inputA = input('이름 입력(exit 입력 시 종료):')

    if inputA == 'exit':
        break

print('----B반 출석 입력----')
inputB = input('이름 입력(exit 입력 시 종료:)')

while True:
    classB.update({inputB})
    inputB = input('이름 입력(exit 입력 시 종료:)')
    if(inputB=='exit'):
        break

print('전체 출석 명단: ', classA | classB)
print('두 반 모두 출석:', classA & classB)
print('A반만 출석:', classA-classB)
print('B반만 출석:', classB-classA)
print('A반 출석 인원:', len(classA))
print('B반 출석 인원:', len(classB))
