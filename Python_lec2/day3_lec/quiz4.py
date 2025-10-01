import pandas as pd
import numpy as np

df = pd.DataFrame({
    '이름':['철수','영희','민수','길동','미나','수현'],
    '출석1':[20,np.nan, 15, np.nan, 18, np.nan],
    '출석2':[19,np.nan,14,np.nan,17,np.nan],
    '중간고사':[80,90,np.nan,75,np.nan,88],
    '기말고사':[np.nan,85,88,np.nan,70,np.nan]

})
print(df)

df = df.dropna(subset=['출석1','출석2'], how='all') #how='all' 하면 둘다 nan 일경우 how='any'가 default. 이러면하나라도 포함되면 drop
df= df.fillna({'중간고사':df['중간고사'].mean()})
#df['중간고사'] = df['중간고사'].fillna(df['중간고사'].mean()
df=df.fillna(df.iloc[0].ffill())
#df=df['기말고사']=df['기말고사'].fillna(df['중간고사'])
df['출석평균']=df[['출석1','출석2']].mean(axis=1)
print(df)

#, '기말고사':df.iloc[0].ffill(axis=1)})

