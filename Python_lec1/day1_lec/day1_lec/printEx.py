ivalue1 = 100
fvalue1 = 42.3

print(ivalue1, fvalue1)
print('ivalue1:', ivalue1)
print('ivalue1:', ivalue1, 'fvalue1:', fvalue1) 
#white space between every value THIS IS DEFAULT VALUE!!
#=> ivalue1: 100 fvalue1: 42.3

print(ivalue1, fvalue1, sep='')
#sets separation to no whitespace
# => 10042.3  no white space between 100 & 42.3

print(ivalue1, fvalue1, sep='/')

print(ivalue1, fvalue1, sep=',')

name1 = 'kim'
name2 = 'lee'

print(name1, name2, end='')
#define end feature (new line is default per print())

print(name1, name2, sep=':')
#if so, => kim leekim:lee