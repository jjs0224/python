import pandas as pd

# frame1 = pd.DataFrame({'kdata':['b','b','a','c','a','a','b'],
#                        'data1':range(7)})
# frame2 = pd.DataFrame({'kdata':['a','b','d'],
#                        'data2':range(3)})
#
# print(frame1)
# print()
# print(frame2)
# print('----양쪽모두에 키가 포함되어있어야 조인가능 : inner join(default)----')
# print(pd.merge(frame1, frame2, on='kdata'))
# print()
# print('----하나라도 포함된데이터 다 merge 하기 : outer join----')
# print(pd.merge(frame1, frame2, on='kdata', how='outer'))
# print()
# print('----left join----')
# print(pd.merge(frame1, frame2, on='kdata', how='left'))
# print()
# print('----right join----')
# print(pd.merge(frame1, frame2, on='kdata', how='right'))



print('-----key 가 다를경우, 키 지정해주기-----')
frame3 = pd.DataFrame({'lkdata':['b','b','a','c','a','a','b'],
                       'data1':range(7)})
frame4 = pd.DataFrame({'rkdata':['a','b','d'],
                       'data2':range(3)})

print('----이렇게 키를 지정해주면 두데이터의 lkdata, rkdata 가 다포함됨---')
print(pd.merge(frame3, frame4, left_on='lkdata', right_on='rkdata'))
print()

print('----동일하게 두개 다 포함되서 하나 빼주기----')
print(pd.merge(frame3, frame4, left_on='lkdata', right_on='rkdata').drop('rkdata',axis=1))
print()


























