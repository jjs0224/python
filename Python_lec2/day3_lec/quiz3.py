import pandas as pd

data = {
    '상품': ['노트북', '키보드', '마우스','모니터','헤드셋'],
    '매출': [1200, 150, 100, 800, 300],
    '판매수량':[30, 200, 300, 50, 120]
}

print('===원본 데이터===')
frame = pd.DataFrame(data, index=['A001','A002','A003','A004','A005'])
print(frame)

print(frame.sort_values(by='매출', ascending=False))
print()
print(frame.sort_values(by='판매수량'))

print(frame.sort_index(ascending=False))

top = frame.sort_values(by='매출', ascending=False)
print(top.head(3))

