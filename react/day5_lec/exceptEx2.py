ldata = [10, 20, 30]

try:
    index, dvalue = list(map(int, input('인덱스와 나눌 숫자를 입력하세요').split()))
    print(ldata[index] / dvalue)
except ZeroDivisionError as e:
    print('숫자는 0으로 나눌 수 없습니다.', e)
except IndexError as e:
    print('잘못된 인덱스 입니다..', e)

