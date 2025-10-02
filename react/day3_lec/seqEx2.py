ldata1 = [10, 20, 30]
ldata2 = [50, 60]
print(ldata1 + ldata2) #[10, 20, 30, 50, 60]  like .extend()

tdata1 = 100, 200
tdata2 = 800, 900
print(tdata1 + tdata2) #(100, 200, 800, 900)

sdata1 = 'hello'
sdata2 = 'world'
print(sdata1 + sdata2) #helloworld
print()

print(ldata1 * 3) #[10, 20, 30, 10, 20, 30, 10, 20, 30]
print(tdata1 * 3) #(100, 200, 100, 200, 100, 200)
print(sdata1 * 3) #hellohellohello
print()

ld1 = [0,0]
ld2 = [1,1,1]
initData = ld1 * 2 + ld2 * 2
print(initData) #[0, 0, 0, 0, 1, 1, 1, 1, 1, 1]