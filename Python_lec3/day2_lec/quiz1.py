import matplotlib.pyplot as plt
import pandas as pd
plt.rc('font', family='Malgun Gothic')

data = pd.read_csv('students.csv')
print(data)

my_color = {'여': 'r', '남': 'b'}
my_marker = {1: 'o', 2: 's', 3:'^'}

data['new_color'] = data['성별'].map(my_color)
print(data)
eng_mean = data['영어'].mean()
print(eng_mean)

for idx, finditem in enumerate(data['학년']):

    xdata = data.loc[data['학년'] == finditem, '수학']
    ydata = data.loc[data['학년'] == finditem, '영어']
    plt.scatter(xdata, ydata,
                marker=my_marker[finditem],
                c = data.loc[data['학년'] == finditem, 'new_color'],
                s = data.loc[data['학년'] == finditem, '과학']
                )

for i, row in data.iterrows():
    if row['영어'] >= eng_mean:
        plt.annotate(row['이름'], (row['수학'], row['영어']),
                     textcoords='offset points', xytext=(10,10))

import matplotlib.patches as patches
#patches.Patch 통해 색별로 레이블 만들어주기
plt.legend(handles=[patches.Patch(label='1학년'),
                    patches.Patch(label='2학년'),
                    patches.Patch(label='3학년'),
                    ], loc=0,
                    edgecolor='k') #레전드 테두리색
plt.show()

#------------------강사님 답 ------------------------
# import pandas as pd
# import matplotlib.pyplot as plt
#
# plt.rc('font', family='Malgun Gothic')
#
# # 1. 데이터 읽기
# df = pd.read_csv("students.csv")
#
# # 2. 조건별 속성 설정
# colors = df['성별'].map({'남':'blue', '여':'red'})
# markers = df['학년'].map({1:'o', 2:'s', 3:'^'})
# sizes = df['과학'] * 5   # 점 크기를 과학 점수로 (확대 비율 5배)
#
# # 3. 산점도 그리기 (학년별 marker 분리해서 그려야 함)
# plt.figure(figsize=(10,7))
#
# for grade, marker in {1:'o', 2:'s', 3:'^'}.items():
#     subset = df[df['학년']==grade]
#     plt.scatter(subset['수학'], subset['영어'],
#                 s=subset['과학']*5,
#                 c=subset['성별'].map({'남':'blue','여':'red'}),
#                 marker=marker, alpha=0.6, label=f"{grade}학년")
#
# # 4. 영어 평균 이상인 학생 annotate
# eng_mean = df['영어'].mean()
# for i, row in df.iterrows():
#     if row['영어'] >= eng_mean:
#         plt.annotate(row['이름'], (row['수학'], row['영어']),
#                      textcoords="offset points", xytext=(10,10))
#
# # 5. 라벨/제목/범례
# plt.xlabel("수학 점수")
# plt.ylabel("영어 점수")
# plt.title("학생별 성적 분포 (수학 vs 영어 vs 과학)")
# plt.legend(title="학년",labelspacing=1.5, title_fontsize=14)
# plt.grid(True)
# plt.show()