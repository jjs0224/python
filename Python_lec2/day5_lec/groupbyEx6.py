import pandas as pd

tips = pd.read_csv('tips.csv')

print('====tip_pct (tip percentage of total_bill)계산해서 추가하기====')
tips['tip_pct'] = tips['tip']/tips['total_bill']

print(tips.pivot_table(values=['tip_pct', 'size'],
                       index=['sex','smoker'],
                       aggfunc='mean'))
print()
print(tips.pivot_table(values=['tip_pct', 'size'],
                       index=['sex','smoker'],
                       aggfunc=['mean','std']))

print()
print(tips.pivot_table(values=['tip_pct','size'],
                       index='day',
                       columns='sex',
                       aggfunc='sum'))
