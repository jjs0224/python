import numpy as np
import pandas as pd

tips = pd.read_csv('tips.csv')
#data 불러오면 첫10개정도 찍어주고, info() 찍어서 데이터정보 확인하기
print('===== 데이터 정보 확인 =====')
print(tips.head(10))
tips.info()
print()

print('====tip_pct (tip percentage of total_bill)계산해서 추가하기====')
tips['tip_pct'] = tips['tip']/tips['total_bill']
print(tips.head(10))

grouped = tips.groupby(['sex','smoker'])
grouped_pct = grouped['tip_pct']
print(grouped_pct.mean())
print()
print(grouped_pct.agg('mean'))
print()
print('===== agg() 사용법 =====')
#여러개 사용할때 agg.() 하고 원하는거 나열해주면 한번에 다 뽑을수있음
#tuple 로 넘겨주면 이름을 바꿀수있음.. mean becomes gmean
print(grouped_pct.agg([('gmean','mean'), 'std', 'sum']))
print()
print('===tip 은 맥시멈으로 뽑고, size 는 총 몇명인지 뽑고싶을때===')
print(grouped.agg({'tip':'max', 'size':'sum'}))
print()

print(grouped.agg({'tip_pct':['min','max'],
                   'size':['sum','mean','std']}))



