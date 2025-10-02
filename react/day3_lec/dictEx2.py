d1 = dict(name='kim', age=40, address='seoul')
print(d1) #{'name': 'kim', 'age': 40, 'address': 'seoul'}
print(type(d1)) #<class 'dict'>
print()

d2 = dict([('name','lee'),('age',20),('address','seoul')])
print(d2) #{'name': 'lee', 'age': 20, 'address': 'seoul'}
print()

d3 = dict(zip(['name','age','address'],['choi',22,'incheon']))
print(d3) #{'name': 'choi', 'age': 22, 'address': 'incheon'}