import numpy as np
import pandas as pd

data = pd.read_csv('P00000001-ALL.csv')
data.info()

print(data.cand_nm.value_counts())

parties = {'Bachmann, Michelle':'Republican',
           'Cain, Herman':'Republican',
           'Gingrich, Newt':'Republican',
           'Huntsman, Jon':'Republican',
           'Johnson, Gary Earl':'Republican',
           'McCotter, Thaddeus G':'Republican',
           'Obama, Barack':'Democrat',
           'Paul, Ron':'Republican',
           'Pawlenty, Timothy':'Republican',
           'Perry, Rick':'Republican',
           "Roemer, Charles E. 'Buddy' III":'Republican',
           'Romney, Mitt':'Republican',
           'Santorum, Rick':'Republican'}

occ_mapping = {
    'INFORMATION REQUESTED PER BEST EFFORTS':'NOT PROVIDED',
    'INFORMATION REQUESTED':'NOT PROVIDED',
    'INFORMATION REQUESTED (BEST EFFORTS)':'NOT PROVIDED',
    'C.E.O':'CEO',
    'C.E.O.':'CEO'
}

data['party'] = data.cand_nm.map(parties)
print(data)
print(data.head())

data = data[data.contb_receipt_amt > 0]
print(data)

print(data.contbr_occupation.value_counts()[:20])
def occ_map(x):
    return occ_mapping.get(x, x)
data.contbr_occupation = data.contbr_occupation.map(occ_map)
print(data.contbr_occupation.value_counts()[:20])

by_occu = data.pivot_table(values='contb_receipt_amt',
                           index='contbr_occupation',
                           columns='party',
                           aggfunc='sum')
print(by_occu)

sum_occ = by_occu[by_occu.sum(axis=1)>2000000]
print(sum_occ)

data_mrbo = data[data.cand_nm.isin(['Obama, Barack','Romney, Mitt'])]
print(data_mrbo.cand_nm.unique())

















