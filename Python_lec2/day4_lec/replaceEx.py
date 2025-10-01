import numpy as np
import pandas as pd

data = pd.Series([1,-999,2,-999,-1000,3])
print(data)




print('--(-999),(-1000)값을 Nan 값으로 바꾸기(.replace())---')
print(data.replace([-999,-1000], np.nan))







print('---특정한값을 각자따로 바까줄값정해주기(-999는 NaN 값으로, -1000은 0으로---')
print(data.replace({-999:np.nan, -1000:0}))
