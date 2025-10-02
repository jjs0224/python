#세트의 특징
#1.중복저장 x
#2.저장순서 x

sdata1 = {'lee', 'choi', 'kim', 'oh', 'kim', 'lee'}
print(sdata1)  #{'choi', 'lee', 'oh', 'kim'}
print(type(sdata1)) #<class 'set'>
sdata2 = {7,1,5,2,6,1,2,4,5,4}
print(sdata2) #{1, 2, 4, 5, 6, 7}

sdata3 = set([3,2,1,4,1,2,3])
print(sdata3) #{1, 2, 3, 4}
print(set('hello')) #{'o', 'h', 'l', 'e'}

sdata4 = {}
print(type(sdata4)) #<class 'dict'> {} 얘를 dict 랑 같이쓰기때문에 클라스가 이걸로 지정됨
sdata5 = set()
print(type(sdata5)) #<class 'set'> 비어있는객체만들고싶으면 꼭 set 선언해줘야함
print(sdata5) #set()