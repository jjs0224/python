import numpy as np
import matplotlib.pyplot as plt
from PIL.ImageOps import cover

label_list = ['Iris-setosa', 'Iris-versicolor','Iris-virginica']
#데이터안에 꽃이름=문자열도있어서 이걸 인덱스(숫자) 로 바꿔주는 함수를 만들어줘야한다
def read_label(label):
    return label_list.index(label)

data = np.loadtxt('iris.data.txt',
                  delimiter=',',
                  converters={4:read_label}) #네번째 열은 (column) 인덱스(숫자로)바꿔줘라
print(data)

color_set = ['b','g','r']
color_list = [color_set[int(label)] for label in data[:, 4]]

plt.scatter(data[:,0], data[:,1], color=color_list)

#인위적으로 legend 만들어주기.. 위에 코드는 color_list 를 레전드로 표현할수없음

import matplotlib.patches as patches

plt.legend(handles=[patches.Patch(color='b', label='iris-setosa'), #각 종류별로 레전드 만들어주기
                    patches.Patch(color='g', label='iris-versicolor'), #색별로 꽃이름지정해주기
                    patches.Patch(color='r', label='iris-virginica'),
                    ], loc='best',
                    edgecolor='k') #레전드 테두리색
plt.show()














