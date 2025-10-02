def personal_info(name, age, address):
    print('name:', name)
    print('age:', age)
    print('address:', address)

personal_info('kim', 20, 'incheon') #name: kim
                                    #age: 20
                                    #address: incheon

personal_info(name='lee', age=30, address='seoul')  #name: lee
                                                    #age: 30
                                                    #address: seoul

personal_info(age=30, name='lee', address='seoul') #keyword type 으로 사용하면 순서바껴도상관없음-> 키위드에맞춰서 값이 지정됨 (for c++, not allowed)
           
d1 = {'name':'choi', 'age':40, 'address':'daegu'}
personal_info(name='choi', age=40, address='daegu')
personal_info(**d1)

def personal_info2(**kwargs):
    print(kwargs)
    print(type(kwargs))

personal_info2(name='choi', age=50) 
    #{'name': 'choi', 'age': 50}                                                                                          
    #<class 'dict'>

def personal_info2(**kwargs): #딕셔너리 형태로 가져와서 언패킹할수있음... 
    for k, v in kwargs.items():  #여기에 k 에는 key, v 에는 value를 넣어줌... 
        print(k,v)
    print()

personal_info2(name='choi', age=50) 
personal_info2(name='choi', age=50, address='seoul')
personal_info2(name='choi', age=50, address='seoul', id=3232)

