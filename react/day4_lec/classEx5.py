class Person3:
    bag = [] #public

    def put_bag(self, stuff):
        #self.bag.append(stuff)
        Person3.bag.append(stuff) #to show its shared/public, this method is RECOMMENDED 

james = Person3()
james.put_bag('book')

print(james.bag)

maria = Person3()
maria.put_bag('key')
print(maria.bag) #['book', 'key']
print(james.bag) #['book', 'key']
print(Person3.bag) #['book', 'key'] RECOMMENDED way to show bag is public and shared between all 

#-------IF YOU WANT SEPARATE BAG FOR EACH OBJECT-----------

class Person3:
    bag = [] #public

    def __init__(self):
        self.my_bag = []

    def put_bag(self, stuff):
        #self.bag.append(stuff)
        self.my_bag.append(stuff) #each object now gets own list of bag
        Person3.bag.append(stuff) #to show its shared/public, this method is RECOMMENDED 

james = Person3()
james.put_bag('book')

print(james.bag)

maria = Person3()
maria.put_bag('key')
print(maria.my_bag) #['key']  each get their own bag
print(james.my_bag) #['book']
print(Person3.bag) #['book', 'key'] RECOMMENDED way to show bag is public and shared between all 