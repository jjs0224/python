import pandas as pd

#
# frame = pd.read_excel('data/monthly_sales.xlsx')
# print(frame)
# print()
#
# print('---header 랑 index 다시 지정해주기---')
# frame = pd.read_excel('data/monthly_sales.xlsx', header=1, index_col=0)
# print(frame)


print('----excel 안에 목록이 2개일경우 따로불러오는법과, 다같이 읽어오기----')
frame2 = pd.read_excel('data/class_info.xlsx',
                       header=0,
                       sheet_name='2학년') #목록이름으로 구별해서가져오기
print(frame2)
print()

frame2 = pd.read_excel('data/class_info.xlsx',
                       header=0,
                       sheet_name=0) #목록도 다 index 로읽을수있는데 0= 첫번째꺼 가져오기
print(frame2)
print()
frame2 = pd.read_excel('data/class_info.xlsx',
                       header=0,
                       sheet_name=None) #모든거 다 불러오기 = 딕셔너리 객채로 불러옴
print(frame2)
print()



print('-------키 이름 정해주고 딕셔너리 형태로 불러오기------')
frame2 = pd.read_excel('data/class_info.xlsx',
                       header=0,
                       sheet_name=['1학년','2학년']) #목록이름을 키값으로해서 딕셔너리형태로 불러오기
print(frame2)
print()



import numpy as np
frame3 = pd.DataFrame(np.random.randn(100,4),
                      columns=['seoul','busan','incheon','suwon'])
print(frame3)
frame3.to_csv('sfile.csv') # index 자동생성됨

frame3.to_csv('sfile2.csv', index=False) # index 없이 파일생성






















































