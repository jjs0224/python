import numpy as np
import pandas as pd

students = pd.DataFrame({
    "학번": [101,102,103,104,105,106,107,108,109,110],
    "이름": ["김철수","이영희","박민수","최지훈","정은지",
           "오하늘","신동엽","한가인","유재석","장동건"],
    "학년": [1,1,1,2,2,2,3,3,3,3],
    "반": [1,1,2,1,2,2,1,1,2,3],
    "국어": [85,90,75,88,95,66,72,80,77,92],
    "영어": [80,70,85,92,88,74,69,83,91,87],
    "수학": [90,85,70,95,99,64,78,88,84,93],
    "과학": [78,82,91,85,90,60,72,89,95,97]
})

clubs = pd.DataFrame({
    "학번": [101,102,103,104,105,106,107,108,109,110],
    "동아리": ["축구","미술","축구","음악","미술",
             "바둑","음악","미술","축구","음악"],
    "출석일수": [15,12,10,18,14,9,17,13,20,16]
})

print(students)
print()
print(clubs)

students_year = students.groupby('학년')

student_id = students.groupby('학년')['국어'].mean()
print(student_id)

q2 = students.pivot_table(values=['수학','영어'],
                          index=['학년','반'],
                          aggfunc='mean')
print(q2)

q3 = pd.merge(students,clubs)
print(q3)
q3_group=q3.groupby('동아리')[['출석일수','과학']].mean()
print(q3_group)


students['평균'] =students[['국어','영어','수학','과학']].apply(lambda x: sum(x)/4, axis=1)
print(students)

grade = [0,60,70,80,90,100]
labels=['F','D','C','B','A']
students['학점']=pd.cut(students['평균'], bins=grade, labels=labels)
print(students)

q5 = q3.pivot_table(values=['국어','영어'],
                          index=['학년','동아리'],
                          aggfunc='mean')
print(q5)

def rate(x):
    if x>15:
        return '우수'
    else:
        return '보통'

q3['출석등급'] = q3['출석일수'].apply(rate, axis=1)

# def calc_avg(x):
#     return sum(x)/4

# students['평균'] = students_year['수학'].apply(calc_avg)
