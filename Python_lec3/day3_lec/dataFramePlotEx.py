import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

np.random.seed(777)
frame = pd.DataFrame(np.random.rand(5,3),
                     index=['customer1','customer2','customer3','customer4','customer5'],
                     columns=['metric1','metric2','metric3'])
print(frame)
#graph figure size 지정하기 (공간을 몇개로나눌건지랑, 사이즈)
#(ax1, ax2) 언패킹을통해 이 두개의 주소값을 가져옴
fig, (ax1,ax2) = plt.subplots(1,2,figsize=(10,7))
#첫번째 그래프(kind=어떤그래프인지(bar), ax=어디위치에 둘건지 꼭지정하기(ax1)
frame.plot(kind='bar', ax=ax1, alpha=0.7, title='bar plot')
ax1.set_xlabel('customer')
ax1.set_ylabel('value')
#xticklabels() 인덱스값을통해 지정해준 xtick 을 이걸로통해 설정할수있음..
plt.setp(ax1.get_xticklabels(), rotation=45)

#두번째 그래프(kind='box')=>box and whiskers graph 그리기
colors=dict(boxes='blue',whiskers='orange', medians='red', caps='k')
#colors 딕셔너리를통해 스타일링 적용시키기
frame.plot(kind='box', ax=ax2, title='box plot', color=colors)
ax2.set_xlabel('metrics')
ax2.set_ylabel('value2')
plt.show()