import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#plt.rc('font', family='Malgun Gothic')
#
# x = np.random.randn(10000)
# #bins 는 잘 선택해서 사용해야함.. 너무적게잡으면 너무두껍게잡히고 너무 크게잡으면 너무 삐죽삐죽거림
# .hist() 통해서 히스토그램 그래프 그리기
# plt.hist(x, bins=100, density=True)
# plt.show()

human = pd.read_csv('human_height.csv')
human.info()
man = human['man']
woman = human['woman']

plt.figure(figsize=(10,7))
plt.hist(man, bins=20, alpha=0.5, label='man',rwidth=1)
plt.hist(woman, bins=20, alpha=0.5, label='woman',rwidth=1)

plt.xlabel('height')
plt.ylabel('frequency')
plt.title('man height distribution')
plt.show()