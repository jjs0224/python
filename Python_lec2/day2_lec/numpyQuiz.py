import numpy as np

x, y = input('학생수, 과목수: ').split()
eachS = 0
score = []
while eachS < int(x):
    score.append(input().split())
    eachS += 1

scores = np.array(score, dtype = np.int32)
print(scores)

for i in scores:
    print(f'student{i+1}: 평균:{i.mean():.2f} '
          f'표준편차:{i.std():.2f} '
          f'최고={i.max()}'
          f'최저={i.min()}'
          )


print(f'{np.mean(scores):.2f}')
print(f'{np.var(scores):.2f}')
print(f'{np.median(scores):.2f}')




for i in scores:
    grades = np.where(i.mean() >= 90, 'A',
                np.where(i.mean() >= 80, 'B',
                np.where(i.mean() >= 70, 'C',
                np.where(i.mean() >= 60, 'D', 'F'))))

    print(f'학생{i}: {grades}')
