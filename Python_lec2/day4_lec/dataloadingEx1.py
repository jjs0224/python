

import pandas as pd

frame1 = pd.read_csv('data/ex1.csv') #header가 포함되어있는 파일 불러오기
print(frame1)
print(type(frame1))


#csv 에 첫줄은 무조건 헤더로 읽어들임..
#첫줄이 헤더가 없을경우 헤더는 없다고 선언해줘야함
print('------헤더없는 csv 파일불러올때 헤더 지정해주는방법-----')
frame2 = pd.read_csv('data/ex2.csv') #header 없는파일 불러오면 데이터잘못표현됨
print(frame2)
frame2 = pd.read_csv('data/ex2.csv', header=None) #헤더없다고해서 제대로불러오기
print(frame2)
frame2 = pd.read_csv('data/ex2.csv', names=['one','two','three','four','msg']) #헤더이름 따로 지정해주기
print(frame2)


print('-------파일자체에 인덱스가있을때 그걸 인덱스로 지정해주기------')
frame3 = pd.read_csv('data/ex2.csv', names=['one','two','three','four','msg'],
                     index_col='msg') #column name 으로 지정해주기
print(frame3)
frame3 = pd.read_csv('data/ex2.csv', names=['one','two','three','four','msg'],
                     index_col=4) #column 인덱스번호로 지정해주기 == 인덱스4번이
print(frame3)




print('-----필요하지않은 줄 빼고 불러오고싶을때-----')
frame4 = pd.read_csv('data/ex4.csv', skiprows=[0,2,3])
print(frame4)