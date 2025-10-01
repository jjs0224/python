import pandas as pd
import numpy as np

scores = pd.Series([70,88,92,54,34,76,59,91,83,78,61,55],
                   index=['홍길동','이순신','임꺽정','정난정','이이','이황',
                          '정도전','이성계','김유신','김철수','정약용','정약전'])
grade=[0,60,70,80,90,100]
print(scores)
grading=(pd.cut(scores,grade,right=False,labels=['F','D','C','B','A']))
print(grading.value_counts())
scores=pd.concat([scores,grading], axis=1, keys=['점수','학점'])
print(scores)
