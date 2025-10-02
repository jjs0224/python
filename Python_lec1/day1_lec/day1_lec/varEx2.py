x, y, z = 10, 20, 30

print(x)
print(y)
print(z)

a = b = c = 100
print(a)
print(b)
print(c)

v1, v2 = 100, 200
v1, v2 = v2, v1 #이렇게하면 값이 바뀜..(by reference)
print(v1)
print(v2)
print()

v3 = v1 + v2
print(v3)
print()

a, b = 10, 20
print(a)
a += b
print(a)

print()
value1 = 10
print(value1/4) # => 2.5
print(value1//4) # => 2 (소수자리날려버림)
print(value1 * value1 * value1)
print(value1 ** 3) # => value1을 세번곱해줌(지수승)

