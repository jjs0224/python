import numpy as np
import pandas as pd

sd1 = pd.Series(np.arange(5), index=list('abcde'))
print(sd1)
print()

print(sd1.drop(['c', 'e']))
print()
print(sd1)

sd1.drop(['c','e'], inplace=True)
print(sd1)
print()

frame = pd.DataFrame(np.arange(16).reshape(4,4),
                     index=list('abcd'),
                     columns=['one','two','three','four'])
print(frame)
print()
print(frame.drop('a'))
print()
print(frame.drop('two',axis=1))
print(frame.drop('two', axis='columns')) #columns 측에있는 two 를 드랍하겠다
print(frame.drop(index='a', columns='one'))