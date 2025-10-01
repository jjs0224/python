import pandas as pd
import matplotlib.pyplot as plt

diamonds = pd.read_csv('diamonds.csv')
diamonds.info() #RangeIndex: 53940
#--diamonds 모든 샘플에서 10퍼센트(frac) 랜덤값을(random_state) 가져옴
diamonds = diamonds.sample(frac=0.01, random_state=49)
diamonds.info() #Index: 539  랜덤으로 10퍼센트 데이터만 불러옴
print('----- cut의 종류 알아보기 (.unique() -----')
print(diamonds.cut.unique())
cut_list = diamonds.cut.unique() #cut 의 종류를 list 형태로 저장해주기
my_color = ['r', 'g', 'b', 'y', 'm'] #색상 사용할 리스트
print('----- cut 종류별로 키로 정해주고, 색을 벨류로 지정해주는 딕셔너리 만들기 -----')
cut_dict = {cut_list[idx]: my_color[idx] for idx in range(len(cut_list))}
print(cut_dict)
print('---newcut column 을 만들어주고 "cut" 행에있는 데이터를 기준으로 딕셔너리사용해 색상정해주기---')
diamonds['newcut'] = diamonds['cut'].map(cut_dict)
print(diamonds.head()) #to check if data has been inputted correctly by checking first 5 data

#table: width of top of diamond relative to widest point (43–95)
#table 값별로 마커사이즈 지정해주려고 함수 만들어주기
def recode_table(table):
    if table >= 60: #테이블안에있는 값이 60 이상이면 100을 리턴한다
        return 100
    elif table >= 58: #테이블안에있는 값이 58 이상이면 30을 리턴한다
        return 30
    elif table >= 54: #테이블안에있는 값이 54 이상이면 5을 리턴한다
        return 5
    else:
        return 1 #54보다 작으면 1 리턴

#newtable column 만들어주고 그안에 값은 'table'행 값기준으로 recode_table 함수를통해 값받기
#table 값이 클수록 newtable 값이 큼..
diamonds['newtable'] = diamonds['table'].apply(recode_table)
print(diamonds.head()) #check if new data has been added correctly

fig = plt.figure(figsize=(8,6)) #그래프의 figsize 지정해주기
ax1 = fig.add_subplot(111)
xdata = diamonds['price'] #x값은 diamonds의 'price' 값들
ydata = diamonds['depth'] #y값은 diamonds의 'depth' 값들

#모든 값들 scatter 해주기. 이때 각 scatter 의 사이즈는 'newtable'기준, color='newcut'기준, alpha=투명도
ax1.scatter(xdata, ydata, s=diamonds['newtable'], c=diamonds['newcut'], alpha=0.7)
plt.xlabel('price')
plt.ylabel('depth')

#레전드 만들어주기
import matplotlib.patches as patches
#patches.Patch 통해 색별로 레이블 만들어주기
plt.legend(handles=[patches.Patch(color='r', label='Very Good'),
                    patches.Patch(color='g', label='Good'),
                    patches.Patch(color='b', label='Ideal'),
                    patches.Patch(color='y', label='Premium'),
                    patches.Patch(color='m', label='Fair'),
                    ], loc='best',
                    edgecolor='k') #레전드 테두리색
plt.show()





















