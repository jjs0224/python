def add(n1, n2):
    return n1+n2

print(add(10, 20))
print(add(10, 20, 30)) #TypeError: add() takes 2 positional arguments but 3 were given

def print_number(v1, v2, v3):
    print(v1)
    print(v2)
    print(v3)

print_number(10, 20, 30)

data = [10, 20, 30]
print_number(*data) #*를 변수앞에 붙히면 리스트 튜플이란것을 언패킹하겠다는뜻

def print_number2(*var):
    # print(var) #(10, 20)
    # print(type(var)) #<class 'tuple'>

    for data in var:
        print(data) 

print_number2(10, 20)   #10
                        #20
print_number2(10, 20, 30, 40)   #10
                                #20
                                #30
                                #40

def add2(*args):
    result = 0
    for d in args:
        result += d
    return result

print(add2(10,20)) #30
print(add2(10,20,30)) #60
print(add2(10,20,30,450)) #510