d1 = {'name':'kim', 'age':30, 'address':'seoul'}
print(d1) #{'name': 'kim', 'age': 30, 'address': 'seoul'}
print(type(d1)) #<class 'dict'>

d2 = {100:'hundred', False:0, 3.5:[3.5, 3.5]}
print(d2) #{100: 'hundred', False: 0, 3.5: [3.5, 3.5]}
print()

#key value 사용해서 그 값 불러오기
print(d1['name']) #kim
print(d2[100]) #hundred
print(d2[False]) #0
print(d2[3.5]) #[3.5, 3.5]