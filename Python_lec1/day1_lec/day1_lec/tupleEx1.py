# tdata1 = (10, 20, 30, 60, 90)
# print(tdata1)
# print(type(tdata1))  #<class 'tuple'>
# tdata2 = ('kim', False, 3232, 95.23)
# print(tdata2)
# print(tdata2[0])
# print(tdata2[1])
# print(tdata2[2]) #3232
# print(tdata2[3]) #95.23
# print()

# print(tdata2[-1]) #95.23
# print(tdata2[-2]) #3232
# print(tdata2[-3]) #False
# print(tdata2[-4]) #kim

# print(tdata2[1:3]) #(False, 3232)

# tdata3 = ( 90, 10, 40)
# print(tdata3)

# tdata4 = 90, 10, 40 #packing
# print(tdata4)
# print(type(tdata4)) #<class 'tuple'>
# print()

# x, y, z = tdata4 #unpacking 한다는 표현을 사용
# print(x)
# print(y)
# print(z)
# print()

# ldata1 = ['kim', 'oh', 'hyo'] #packing
# name1, name2, name3 = ldata1 #unpacking 한다는 표현을 사용
# print(name1)
# print(name2)
# print(name3)

# a, b, c = 10, 20, 30

# x, y = 100, 200
# y, x = x, y #create new tuple(100, 200) then use unpacking to load values into y and x
# print(x) #200
# print(y) #100

tdata5=10
print(type(tdata5))
sdata2= tdata5
sdata1 = tuple([sdata2, tdata5])
print(sdata1)
print(type(sdata1))