d1 = {'name':'hyo', 'age':16}
print(d1)
print(d1['name']) #hyo
print(d1.get('name')) #hyo
print()

#print(d1['address']) #KeyError: 'address' 키값이 존재하지않아서 에러
print(d1.get('address')) #None
print(d1.get('address', 'busan')) #busan
print()

print(d1.keys()) #dict_keys(['name', 'age'])
print(d1.values()) #dict_values(['hyo', 16])
print(d1.items()) #dict_items([('name', 'hyo'), ('age', 16)])

for k in d1.keys():
    print(k) #name
             #age

for v in d1.values():
    print(v)  #hyo
              #16

for i in d1.items(): #item 은 튜플로 가져옴 => unpacking 가능
    print(i) #('name', 'hyo')
             #('age', 16)
print()

for k, v in d1.items():
    print(k, v, sep=':')  #name:hyo
                          #age:16

