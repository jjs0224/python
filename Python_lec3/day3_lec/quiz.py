import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
plt.rc('font', family='Malgun Gothic')

data = pd.read_csv('students_scores.csv')
print(data)

year1 = data.loc[data['학년'] == 1, '수학']
# year1.index.name = '1학년'
print(year1)
year2 = data.loc[data['학년'] == 2, '수학']
year2.index.name = '2학년'
year3 = data.loc[data['학년'] == 3, '수학']
year3.index.name = '3학년'
fig = plt.figure(figsize=(10,8))
ax1 = fig.add_subplot(111)
box = ax1.boxplot([year1, year2, year3], labels=['1학년','2학년','3학년'],
            showmeans=True,  whiskerprops=dict(color='r', linestyle='--'), patch_artist=True)
plt.grid(axis='y', linestyle='--')

colors = ['lightblue','lightgreen','lightpink']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

plt.show()



# import pandas as pd
# import matplotlib.pyplot as plt
#
# plt.rc('font', family='Malgun Gothic')
#
# import pandas as pd
# import matplotlib.pyplot as plt
#
# # 1. 데이터 읽기
# df = pd.read_csv("students_scores.csv")
#
# # 2. groupby + apply(list)로 학년별 수학 점수 그룹화
# data = df.groupby('학년')['수학'].apply(list)
#
# # 3. boxplot 그리기
# plt.figure(figsize=(8,6))
# box = plt.boxplot(
#     data.values,                             # 리스트 값만 전달
#     labels=[f"{g}학년" for g in data.index], # 학년 인덱스로 라벨 지정
#     patch_artist=True,   # 박스 색 채우기
#     showmeans=True       # 평균 표시
# )
#
# # 4. 박스 색상 지정
# colors = ['lightblue', 'lightgreen', 'lightpink']
# for patch, color in zip(box['boxes'], colors):
#     patch.set_facecolor(color)
#
# # 5. 제목, 라벨
# plt.title("학년별 수학 점수 분포", fontsize=14, fontweight='bold')
# plt.xlabel("학년")
# plt.ylabel("수학 점수")
# plt.grid(True, axis='y', linestyle='--', alpha=0.7)
# plt.show()
