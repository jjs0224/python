import numpy as np
import pandas as pd


frame = pd.DataFrame(np.random.randn(1000,3),
                     columns=['first','second','third'])
print(frame)
frame.iloc[:4, [1,2]] = np.nan
print()
print(frame)
print()

print(frame.sum(skipna=False))
print()
print(frame.mean())
print()
print(frame.std())
print('--describe--')
print(frame.describe())
print('---info()---')
frame.info()
print()

print(frame.head(15)) #데이터가너무많을때 default 5줄만보여주는데 이거정해주기.head
print(frame.tail(15)) #데이터 끝에서부터 15줄 가져오기

