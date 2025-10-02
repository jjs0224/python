try:
    x = int(input('나눌 숫자를 입력하세요:'))  
    y = 10 / x

except:
    print('예외 발생!!!!!!')

else: 
    print(y) #예외없이 트라이부분에서 에러가없으면 여기로넘어와서 실행됨

finally:
    print('무조건 실행') #에러가 나든 안나든 실행

print('프로그램 종료')