import numpy as np
import pandas as pd

df = pd.DataFrame({
    '이름':['철수','영희','민수'],
    '수학':[90, 85, 75],
    '영어':[88,92,67],
    '과학':[95,80,85],
})
print(df)
print()
print('---수학,영어,과학도 인덱스로 스택해줌---')
stacked = df.set_index('이름').stack()
print(stacked)

print('---데이터프레임으로 만들기(초기화시켜줌)---')
df_reset = stacked.reset_index()
print(df_reset)
print()

print('---df_reset 의 콜롬 네임들출력해서 확인하기---')
print(df_reset.columns)
print()

print('---df_reset 콜럼이름 바꿔주기---')
df_reset.columns = ['이름','과목','점수']
print(df_reset)

