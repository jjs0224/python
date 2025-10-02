def stats_func(*data):
    if not data:
        return f'sum:0 avg:None max:None min:None'
    
    total = sum(data)
    avg = total/len(data)
    maximun = max(data)
    minimum = min(data)

    return f'sum:{total} avg:{avg} max:{maximun} min:{minimum}'

user_input = input('숫자들을 입력하세요(공백으로 구분):')
numbers = list(map(int, user_input.split()))

result = stats_func(*numbers)

print('\n 통계 결과: ', result)