ldata = [10,40,20]

# for d in ldata:
#     print(d)

# it = ldata.__iter__()
# print(it)
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())

# it2 = range(3).__iter__()
# print(it2)
# print(it2.__next__())
# print(it2.__next__())
# print(it2.__next__())
# print(it2.__next__())

# it3 = 'Hello'.__iter__()
# print(it3)
# print(it3.__next__())
# print(it3.__next__())
# print(it3.__next__())
# print(it3.__next__())
# print(it3.__next__())
# print(it3.__next__())

d1 = {'name':'kim', 'age':20, 'address':'busan'}
# print(d1.keys())
# for k in d1.keys():
#     print(k)

it5 = d1.keys().__iter__()
print(it5)
print(it5.__next__())
print(it5.__next__())
print(it5.__next__())

s1 = {3,2,4,1}
ld2 = list(s1)
print(ld2)