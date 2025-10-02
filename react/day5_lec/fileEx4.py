infile1 = open('data/USPres.txt', 'r') 
infile2 = open('data/VPres.txt', 'r') 

pdata = [line for line in infile1]

outfile = open('Both.txt', 'w')
for vice in infile2:
    if vice in pdata:
        outfile.write(vice)

infile1.seek(0) #아까읽어줬기때문에 포인트를 다시 처음으로 잡아주기
infile2.seek(0) #아까읽어줬기때문에 포인트를 다시 처음으로 잡아주기
file1 = {line for line in infile1} #세트에 모든 밸류를 넣어줌
file2 = {line for line in infile2} #세트에 모든 밸류를 넣어줌

bothData = file1 & file2 #교집합
slist = sorted(bothData) #set sorting 하는 방법=> list 로 돌려줌

outfile2 = open('Both2.txt', 'w') #새로운파일경로오픈 => 쓰기전용으로 세팅
outfile2.writelines(slist) #여러줄적어주는거기때문에 .writelines() 사용해서 파일에 정보를 write

outfile2.close() #파일꼭닫아주기
outfile.close()
infile1.close()
infile2.close()