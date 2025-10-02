def printInsa():
    print('hello')

printInsa() #hello

def add(num1, num2):
    print('{} + {} = {}'.format(num1, num2, num1+num2)) 
    print(f'{num1} + {num2} = {num1+num2}') #100 + 200 = 300
add(100,200) #100 + 200 = 300

def subtract(num1, num2):
    return num1 - num2

sresult = subtract(200, 900)
print(sresult) #-700