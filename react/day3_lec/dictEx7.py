d1 = {
    'name'   :'kim',
    'address':'busan',
    'scores' :{
        'kor':90,
        'eng':80,
        'math':100
    }
}

print(d1) #{'name': 'kim', 'address': 'busan', 'scores': {'kor': 90, 'eng': 80, 'math': 100}}

print(d1['name']) #kim
print(d1['address']) #busan
print(d1['scores']) #{'kor': 90, 'eng': 80, 'math': 100}
print(d1['scores']['eng']) #80

d2 = {'a':10, 'b':20, 'c':30, 'd':40, 'e':50}
d3 = d2 #주소를 가져가기때문에 이 두 변수는 같은 주소로향해서 하나바꾸면 다 바뀜
d3['b'] = 5000
print(d2) #{'a': 10, 'b': 5000, 'c': 30, 'd': 40, 'e': 50}
print(d3) #{'a': 10, 'b': 5000, 'c': 30, 'd': 40, 'e': 50}

d4 = d2.copy() #값들을 카피해가기때문에 값을바꿔도 변동되지않음
d4['b'] = 89898
print(d4) #{'a': 10, 'b': 89898, 'c': 30, 'd': 40, 'e': 50}
print(d2) #{'a': 10, 'b': 5000, 'c': 30, 'd': 40, 'e': 50}

d5 = {'a':{'python':'2.7'}, 'b':{'python':3.10}}
d6 = d5.copy()
d5['a']['python'] = '3.12.10'
print(d5) #{'a': {'python': '3.12.10'}, 'b': {'python': 3.1}}
print(d6) #{'a': {'python': '3.12.10'}, 'b': {'python': 3.1}}

import copy
d7 = copy.deepcopy(d5)
d7['a']['python'] = '2.7'
print(d7) #{'a': {'python': '2.7'}, 'b': {'python': 3.1}}
print(d5) #{'a': {'python': '3.12.10'}, 'b': {'python': 3.1}}