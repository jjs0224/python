class Person:
    def greeting(self):
        print('Hello!!!!')

print(Person()) #<__main__.Person object at 0x000002039C9AED40> return address of Object of Person 

obj = Person()
obj.greeting() #Hello!!!!

obj2 = Person()
obj2.greeting() #Hello!!!!

print(type(obj)) #<class '__main__.Person'>
ivalue = 10 
print(type(ivalue))
ldata = [10, 20]
print(type(ldata))
ldata.append(50)