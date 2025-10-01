

import numpy as np
import pandas as pd

data = pd.DataFrame(np.arange(6).reshape(2,3),
                    index=pd.Index(['ohio','colorade'],name='state'),
                    columns=pd.Index(['one','two','three'], name='number'))
print(data)
print()
print('---시리즈형태로 stack 한 데이터---')
result = data.stack()
print(result)
print()
print('---항상 맨 오른쪽에있는 인덱스로 돌림---')
print(result.unstack())
print()
print('---맨첫번째 인덱스(level=0)를 돌림---')
print(result.unstack(level=0))
print()
print('---지정해준 이름 기준으로 돌림(state becomes column name----')
print(result.unstack('state'))
print()



s1 = pd.Series([0,1,2,3], index=list('abcd'))
s2 = pd.Series([4,5,6], index=list('cde'))
print(s1)
print()
print(s2)
print()
print('---concat 사용해서 s1 이랑 s2 더해주기(키이름도 정해줌)---')
data2 = pd.concat([s1,s2],axis=0,keys=['one','two'])
print(data2)
print()
print('---unstack 해서 데이터프래임으로 만들어주기(default로 오른쪽(알파벳)이 가로로됨)---')
print(data2.unstack())
print()
print('---unstack 해서 데이터프레임으로 출력(0으로 지정해주면서 첫번째 인덱스가 가로로 나열됨)---')
print(data2.unstack(level=0))



















