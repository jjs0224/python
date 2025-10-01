import pandas as pd

data = {
    '이름': ['철수','영희','민수'],
    '수학': [90, 60, 100],
    '영어': [80, 75, 95],
    '과학': [70, 85, 90]
}

frame = pd.DataFrame(data)
print(frame)

f1 = lambda x: x[['수학','영어','과학']].sum()

f2 = lambda x: x.mean()
frame['평균']=frame.apply(f1, axis=1)
print(frame)
#
result2 = frame[['수학','영어','과학']].apply(f2, axis=0)
print('[과목별 평균]')
print(result2)

