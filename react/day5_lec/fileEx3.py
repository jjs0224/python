infile1 = open('data/States.txt', 'r')
ldata1 = [line for line in infile1] #줄별로 리스트에 데이터를 가져와서 ldata1(리스트) 에 저장
print(ldata1) #1.

ldata1.sort()
print(ldata1)
infile1.close()

outfile1 = open('StatesAlpha.txt', 'w')
outfile1.writelines(ldata1) #ldata1 에있는 모든정보를 outfile1 에 write 해줌
outfile1.close() #

infile2 = open('data/States.txt', 'r')
ldata2 = [line for line in infile2]

ldata2.sort(key=lambda x : len(x), reverse=True)  #sort 의 기준을 글자수로잡아주고 소팅해줌 
ldata2.sort(key=len, reverse=True) #len 도 함수이기때문에 그냥 이렇게도 사용가능
print(ldata2)

infile2.seek(0) #이걸통해서 읽는포인트를 다시 처음으로 가져와야함
print([line for line in infile2]) #line14. 에 이미 데이터를다 읽으며 넣었을때 다시 프린트하면 아무것도 안뜸
                                #과거에 읽어들이면서 포인트(cursor point)가 맨뒤로가있어서 그거 앞으로 옮겨줘야함(seek)
