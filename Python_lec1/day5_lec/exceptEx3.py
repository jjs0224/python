def three_multiple():
    idata = int(input('3의 배수를 입력하세요:'))
    if idata % 3 != 0:
        raise Exception('입력하신 값은 3의 배수가 아닙니다.')
    print('입력받은 데이터: ', idata)

try:
    three_multiple()

except Exception as e:
    print('예외 발생')
    print('예외 상세 내용: ', e) # e =>raise Exception('입력하신 값은 3의 배수가 아닙니다.')에서 입력한 내용

