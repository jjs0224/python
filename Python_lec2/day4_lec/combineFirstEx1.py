import numpy as np
import pandas as pd

s1 = pd.Series([np.nan, 2.5, np.nan, 4.5, 5.5, np.nan],
               index=list('fedcba'))
s2 = pd.Series(np.arange(len(s1),dtype=np.float32),
               index=list('fedcba'))

print(s1)
print()
print(s2)
print()
print('---.where() 사용해서 null 인경우 s2,로 리플래이스 해주기---')
print(np.where(pd.isnull(s1),s2,s1))
print()
print('----s1에서 nan 값들을 s2에서 불러옴')
print(s1.combine_first(s2))
print()

df1 = pd.DataFrame({'d1':[1., np.nan, 5., np.nan],
                    'd2':[np.nan, 2., np.nan, 6.]})
df2 = pd.DataFrame({'d1':[5., 4., np.nan, 3., 7.],
                    'd2':[np.nan, 3., 4., 6., 8.]})
print(df1)
print()
print(df2)
print()
print('---d1 에서 nan 값들을 d2에서 가져옴..d2 에도 없을경우 NaN---')
print(df1.combine_first(df2))