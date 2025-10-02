x = 10

def foo():
    global x #if global is used, its declaring its going to use x defined outside of function, so when foo is called, it will change x value
    x=20
    print(x) #20

foo()
print(x) #10 they have same name but different variable. changed x value is not returned

def print_hello(): #(2.function is called)
    hello = 'hello python~~~' #(3.declare hello)

    def print_message(): #(declare print_message func)
        print(hello) 

    print_message()

print_hello() #hello python~~~  (1.call print_hello function)

def A(): #2.
    x = 10 #3.

    def B(): #4
        nonlocal x #5 declare its going to use outside variable (in A)
        x = 20 #6.

    B() 
    print(x)

A() #20  1.

def A():
    x = 10
    y = 100
    def B():
        x = 20
        def C():
            nonlocal x #get the top local variable so for this case, use x in B() NOT A()
            nonlocal y #use y variable in A() 
            x = x + 30
            y = y + 300
            print(x)
            print(y)
        C()
    B()
A() #50
    #400   