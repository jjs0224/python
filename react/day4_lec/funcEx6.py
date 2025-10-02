def insa():
    print('helloooooo~~~~')

print(insa) #<function insa at 0x000001C129233E20>
fv = insa #address of insa is copied and now fv becomes insa function
print(fv) #<function insa at 0x0000025AA8403E20>
fv() #helloooooo~~~~ 

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2
def mul(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

flist = [add, sub, mul, divide]

print(flist[1](10, 20)) #-10 

def calc(cf, n1, n2):
    result = cf(n1, n2)
    return result

print(calc(mul, 100, 20))

ldata = [4,1,8,5]
ldata.sort()
print(ldata) #[1, 4, 5, 8] ascending
ldata.sort(reverse=True)
print(ldata) #[8, 5, 4, 1] decending

#-----list with tuple, to sort according to value -----
ldata2 = [('lee', 90),('choi', 100),('kim', 80),('hyo', 88)] #이렇게바로 sort 못함 as more than 1 value in each tuple

def mfunc(x): #this function receives all tuple, and get the key value
    return x[1] #for each tuple, get the value for that key->to be used for sorting

ldata2.sort(key=mfunc) #for every tuple, calls the function mfunc to receive value for each key, and then using that value, sort
print(ldata2) #[('kim', 80), ('hyo', 88), ('lee', 90), ('choi', 100)]

#----sort according to last character of each word----
def f1(x):
    return x[-1]

ldata3 = ['deemcratic', 'sequoia', 'equal', 'brr', 'break', 'two']
ldata3.sort(key=f1)
print(ldata3) #['sequoia', 'deemcratic', 'break', 'equal', 'two', 'brr']
