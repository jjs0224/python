import json
import pandas as pd

obj = """
{"name":"Wes",
 "place_lived":["United States","Spain","Germany"],
  "siblings":[{"name":"scott","age":25,"pet":"zuko"},
              {"name":"kim","age":30,"pet":"kitty"}]
} 
"""
print('-----data 가져오기-----')
data = json.loads(obj)
print(data)
print()
print('----딕셔너리 형태로 가져온거 확인----')
print(type(data))
print()
print('----sibling 키 관련데이터만 출력----')
print(data['siblings'])
print()
print('----silbing 데이터프레임으로 만들기----')
frame = pd.DataFrame(data['siblings'])
print(frame)

