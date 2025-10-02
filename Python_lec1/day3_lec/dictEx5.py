tdata = dict()
while True:
    name = input('이름을 입력하세요: ')
    sdata = list(map(int,input('영어 수학 국어 점수를 입력하세요').split()))
    tdata.update({name:sdata})
    endKey = input('계속 진행하시겠습니까?(y/n)')
    if endKey=='n':
        break
    else:
        continue
print(tdata)

for name, scores in tdata.items():
    total = 0
    for score in scores:
        total += score
    print(f'이름:{name:5} 영어:{scores[0]:5} 수학:{scores[1]:5} 국어:{scores[2]:5}' +
            f'총첨:{total} 평균:{total/3:5.2f}')