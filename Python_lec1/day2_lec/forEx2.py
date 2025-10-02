ldata1 = [40, 20, 90, 70, 30]

for i in ldata1:
    print(i)

print()
tdata1 = 80, 10, 20, 40, 50

for i in tdata1:
    print(i)

print()
for i in reversed(tdata1):
    print(i)

print()
for i in range(2,10,1):
    for j in range(1,10,1):
        print(i,' x ', j, ' = ', i*j)