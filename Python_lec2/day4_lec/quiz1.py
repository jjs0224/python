import pandas as pd

df_students = pd.DataFrame({
    "학번":[101, 102, 103],
    "이름":["철수","영희","민수"],
    "학년":[1,2,1]
})

df_enroll = pd.DataFrame({
    "학번":[101, 101, 102, 103, 103],
    "과목코드":["M101","E101","M101","S101","E101"]
})

df_courses = pd.DataFrame({
    "과목코드": ["M101", "E101", "S101"],
    "과목명": ["수학","영어","과학"],
    "교수": ["김교수","이교수","박교수"]
})
print('----INNERJOIN----')
data = pd.merge(df_students, df_enroll)
print(data)
print('----OUTERJOIN----')
data = pd.merge(data, df_courses, how="outer")
print(data)
print('----수강과목수 count 해주기----')
data["수강과목수"] = data["학번"].map(data["학번"].value_counts())
print(data)