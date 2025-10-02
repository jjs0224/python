# strValue1 = 'hello good day'
# tValue = strValue1.split() #white space 기준(default) 으로 잘라서 list 형태로 만들어줌
# print(tValue)

# strValue2 = '2025/09/16/11/42'
# tValue2 = strValue2.split('/') #/ 기준으로 잘라서 list 형태로 만들어줌
# print(tValue2)

# print(strValue2.split('/',1)) #['2025', '09/16/11/42']
# print(strValue2.split('/',2)) #['2025', '09', '16/11/42']
# print(strValue2.split('/',3)) #['2025', '09', '16', '11/42']  몇번자를건지 지정해줌
# print()

# table = str.maketrans('aeiou', '12345') #make table=a with value 1, e with value 2,,,, 
# print('apple'.translate(table)) #1ppl2  translate a with 1 , ...

ldata1 = ['apple', 'pear', 'grape', 'orange', 'banana']
rStr = ' '.join(ldata1) #apple pear grape orange banana
print(rStr)

rStr = '-'.join(ldata1) #apple-pear-grape-orange-banana
print(rStr)

strValue3 = '     python     '
print('*', strValue3, '*')          #*      python      *
print('*', strValue3.strip(), '*')  #* python *
print('*', strValue3.rstrip(), '*') #*      python *
print('*', strValue3.lstrip(), '*') #* python      *
print()

strValue4 = ',.python.'
print(strValue4) #,.python.
print(strValue4.strip(',.')) #python
print(strValue4.lstrip(',.')) #python.
print(strValue4.rstrip(',.')) #,.python

strValue5 = 'python'
print('*',strValue5,'*')            #* python *
print('*',strValue5.ljust(10),'*')  #* python     *
print('*',strValue5.rjust(10),'*')  #*     python *
print('*',strValue5.center(10),'*') #*   python   *

print('454'.zfill(5)) #00454
