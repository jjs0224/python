import pandas as pd
import numpy as np

data = pd.DataFrame(np.arange(12).reshape(3,4),
                    index=['ohio','colorade','new york'],
                    columns=['one','two','three','four'])
print(data)
print('---map 사용해서 인덱스 다 대문자로바꿔주기---')
data.index=data.index.map(str.upper)
print(data)
print()


print('---rename(index, columns) 사용해서 대문자/소문자로다바꾸기 (title=첫자만대문자)---')
print(data.rename(index=str.title, columns=str.upper))
print()



print('---rename 사용해서 인덱스 이름자체를 바꿔주기(OHIO 를 INDIANA 로바꾸기)---')
print(data.rename(index={'OHIO':'INDIANA'}))
print()



print('---rename(columns=새이름) 사용해서 콜롬이름도 바꿔주기 three->THIRD바꾸기---')
print(data.rename(columns={'three':'THIRD'}))





