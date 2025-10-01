import numpy as np

score_list = []
name_list = []
while True:
    user_name = input('이름을 입력하세요: ')
    user_input = input('국어 영어 수학 점수를 입력하세요:').split()
    name_list.append(user_name)
    score_list.append(user_input)
    endScore = input('입력을 계속 진행하시겠습니까? (y/n)')
    if endScore == 'n':
        break

scores = np.array(score_list, dtype = int)
names = np.array(name_list)
print(scores)
print()

print(f'국어 총점: {scores[:,0].sum(axis=0)},', end=' ')
print(f'영어 총점: {scores[:,1].sum(axis=0)},', end=' ')
print(f'수학 총점: {scores[:,2].sum(axis=0)},')

print(f'수학 점수로 정렬 후')

#print(scores[scores[2].argsort(), : ])
print(scores[scores[:,2].argsort()])

# print(f'국어 총점: {scores.sum(axis=0)[0]},', end=' ')
# print(f'영어 총점: {scores.sum(axis=0)[1]},', end=' ')
# print(f'수학 총점: {scores.sum(axis=0)[2]},')

while True:
    name = input('\n출력할 학생의 이름을 입력하세요: (exit : 종료)')
    if name == 'exit':
        break
    if name in names:
        print(f'{name} 과목점수: {scores[names == name]}', end=' ')
        print(f'평균:{scores[names == name].mean():.2f}', end=' ')
        print(f'표준 편차:{scores[names == name].std():.2f}', end=' ')
        print(f'분산:{scores[names == name].var():.2f}')
    else:
        print(f'입력하신 학생은 존재하지않습니다.')
