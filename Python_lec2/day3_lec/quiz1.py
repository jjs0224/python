import pandas as pd
import numpy as np

data = {
    '번호': [1,2,3,4,5,1,2,3,4,5],
    '반': ['A','A','A','A','A','B','B','B','B','B'],
    '영어': [180, 90, 100, 80, 70, 90, 100, 70, 80, 90],
    '국어': [90, 80, 90, 70, 100, 80, 90, 100, 70, 80],
    '수학': [80, 100, 80, 90, 80, 100, 70, 80, 90, 100]
}

frame = pd.DataFrame(data, columns=['반', '번호', '국어', '영어', '수학'])
print(frame)

frame.drop(['반','번호'], axis=1, inplace=True )


frame['평균'] = frame.mean(axis=1)
frame.loc['평균'] = frame.mean(axis=0)
print(frame)