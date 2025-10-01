


import pandas as pd
import numpy as np

myindex = ['김구','이봉창','안중근','윤봉길']
mycolumns = ['강남구','은평구','마포구','용산구']
mylist = np.reshape(list(10*onedata for onedata in range(1,17)), [4,4])

frame = pd.DataFrame(mylist, index=myindex, columns=mycolumns)
print(frame)

print(frame.iloc[[0]]) #dataframe 0번째 행 가져오기
print()
print(frame.loc[['김구']]) #김구행 가져오기
print()
print(frame.iloc[[1,3]]) #1번과 3번 가져오기
print()
print(frame.loc[['윤봉길']]) #윤봉길행 가져오기
print()
print(frame.loc[['윤봉길','이봉창']]) #윤봉길과 이봉창행 출력하기
print()
print(frame.loc['윤봉길']['은평구']) #윤봉길중 은평구 출력하기
print()
print(frame.loc[['김구','이봉창'],['용산구','은평구']]) #김구에서 이봉창, 용산구에서 은평구
print()
print(frame.loc[frame['은평구']<100]) #은평구중 100보다적은데이터
print()
print(frame.loc[frame['은평구']==100]) #은평구중 100인데이터
print()
frame.loc['김구':'안중근',['용산구']]=80 #김구에서 안중근까지 용산구 다 80으로바꾸기
print(frame) #바꾼값출력
