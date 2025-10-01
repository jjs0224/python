import numpy as np
import pandas as pd

data1 = pd.read_csv('data/students.csv')
data2 = pd.read_csv('data/classes.csv')

frame = pd.merge(data1,data2)

frame=frame.replace({'1반':'A반', '2반':'B반', '김선생':'Kim','이선생':'Lee'})
print(frame)
frame['평균']=frame[['수학','영어','과학']].mean(axis=1)
print(frame)

