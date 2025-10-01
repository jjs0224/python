import numpy as np
import pandas as pd

states = ['ohio','new york','vermont','florida',
          'oregon','nevada','california','idaho']

data = pd.Series(np.random.randn(8), index=states)
data[['vermont','nevada','idaho']] = np.nan
print(data)
print()

print('=== 첫4개 East, 나머지 4개 West 로 구별해주기(라벨링써서) ===')
group_label = ['East'] * 4 + ['West'] * 4
print(group_label)
print()
print('=== East & West 그룹별로 평균값 구해주기 ===')
print(data.groupby(group_label).mean())
print()
print('=== 각 그룹의 NaN 값을 그 그룹의 평균값으로 채워주기 ===')
fill_mean = lambda g: g.fillna(g.mean()) #nan 값 평균값으로 채울 함수
print(data.groupby(group_label).apply(fill_mean))
#각 그룹별로 apply 해줌.. -> East 데이터가 fill_mean 통해 NaN 값 평균값으로채워주고
#                      -> 그다음 West 데이터들을 넘기며 fill_mean 함수가 진행됨

















