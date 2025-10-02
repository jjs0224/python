ldata1 = [10, 20, 30, 40]
print(ldata1)
ldata1.insert(1,  [100, 200]) #.insert('첫번째수는 몇번째의 인덱스인지', 넣을객체)
print(ldata1)                       #[10, [100, 200], 20, 30, 40]

ldata2 = [10, 20, 30, 40]
ldata2[1:1] = [ 100, 200 ]   #ldata2[1:1] <= 주소값을 가져옴... 이경우엔 인덱스 1에서시작해서 1로끝나는지점 
print(ldata2)                 #[10, 100, 200, 20, 30, 40]       ldata2[1:1] 에서가져온주소값에 넣어줌 

rvalue = ldata2.pop()
print(rvalue)  #40
print(ldata2)  #[10, 100, 200, 20, 30]

rvalue = ldata2.pop(1) #1번째의 인덱스값을 pop 해줘라
print(rvalue)  #100
print(ldata2)  #[10, 200, 20, 30]

ldata2.remove(200)
print(ldata2)  #[10, 20, 30]