d1 = {'name':'kim', 'weight':80}
print(d1)
d1['name'] = 'lee' #지정된 키값 밸류 바까줌
print(d1) #{'name': 'lee', 'weight': 80}

d1['height'] = 180 #새로운 키값+밸류 딕셔너리에 추가해줌
print(d1) #{'name': 'lee', 'weight': 80, 'height': 180}
print()

d1.setdefault('address') #set new key value but set the value to none(default)
print(d1) #{'name': 'lee', 'weight': 80, 'height': 180, 'address': None}

d1.setdefault('id',323) 
print(d1) #{'name': 'lee', 'weight': 80, 'height': 180, 'address': None, 'id': 323}

d2 = {'name':'kim', 'weight':80}
d2.update(weight=70)
print(d2) #{'name': 'kim', 'weight': 70}
d2.update(height=170)
print(d2) #{'name': 'kim', 'weight': 70, 'height': 170}
print()

d2.update(name='choi', address='seoul')
print(d2) #{'name': 'choi', 'weight': 70, 'height': 170, 'address': 'seoul'}
print()

d2.update({'name':'lee', 'weight':65, 'id':123}) #key가 존재하면 업데이트해주고 없으면 추가해줌
print(d2) #{'name': 'lee', 'weight': 65, 'height': 170, 'address': 'seoul', 'id': 123}

d2.update([('name', 'oh'),('age',30)])
print(d2) #{'name': 'oh', 'weight': 65, 'height': 170, 'address': 'seoul', 'id': 123, 'age': 30}

rdata = d2.pop('name') #dictionary 에서는 키값을꼭 적어줘야 그 값을삭제시킬수있음
print(rdata) #oh  
print(d2) #{'weight': 65, 'height': 170, 'address': 'seoul', 'id': 123, 'age': 30}

#지우고싶은 키벨류가 딕셔너리에 없을때 디폴트값을 서울로 지정해서 받아옴
print(d2.pop('location','seoul')) #seoul

del d2['weight']
print(d2) #{'height': 170, 'address': 'seoul', 'id': 123, 'age': 30}