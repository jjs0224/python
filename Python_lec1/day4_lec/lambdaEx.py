#lambda : 기준으로 (매개변수) : (return 해줄 값에 사용할식)
#only for basic 

def plus_ten(x):
    return x + 10

print(plus_ten(20)) #30

print (lambda x : x + 10) #<function <lambda> at 0x000001EB838829E0>

lf = lambda x : x + 10 #lambda 는 주소값을 넘겨줌 
print(lf(20)) #30

ladd = lambda n1, n2 : n1 + n2
print(ladd(100,20)) #120

ldata2 = [('lee', 90),('choi', 100),('kim', 80),('hyo', 88)]
ldata2.sort(key=lambda x:x[1]) #간단한 function 람다사용해서 밸류값으로잡아줄수있음
print(ldata2)  #[('kim', 80), ('hyo', 88), ('lee', 90), ('choi', 100)]

ldata3 = [90, 77, 22, 55]
ldata4 = list(map(plus_ten, ldata3))
print(ldata4) #[100, 87, 32, 65]

ldata6 = list(map(lambda x: x + 10, ldata4))
print(ldata6) #[110, 97, 42, 75]