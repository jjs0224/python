import matplotlib.pyplot as plt
import numpy as np

# f1 = plt.figure(figsize=(10, 2))
# #기본단위는 inch 단위 (figsize = (width, height))
# # print(f1) #Figure(1000x200) 사이즈 체크
# plt.title('figsize change', fontsize=14)
# plt.plot(np.random.randn(200))
# plt.show()


x = np.linspace(0, 3, 50)
y1 = np.cos(3 * np.pi * x) * np.exp(-2*x)
y2 = np.cos(3 * np.pi * x)
# 윗부분(top partition 결과값 세팅해주기 .subplot())
axes = plt.subplot(2, 1, 1)
#.subplot( row, column, (row 가 두개만들어졌음으로 여기서 윗부분(1번을가져옴))
# print(axes) #Axes(0.125,0.53;0.775x0.35)
plt.plot(x, y1, 'yo-')
plt.title('multi partition')
plt.xlabel('x1')
plt.ylabel('result1')

# 아래부분(bottom partition 결과값 세팅해주기 .subplot())
plt.subplot(2, 1, 2)
plt.plot(x, y2, 'r-.')
plt.xlabel('time')
plt.ylabel('result2')
#partition 들이 너무붙어있을때 간격띄워주기 방법들 (tight_layout() & subplots_adjust(hspace= ))
#plt.tight_layout() #윗부분 아랫부분 띄워주기(아니면 xlabel 안보임)
plt.subplots_adjust(hspace=0.3)
plt.show()






























