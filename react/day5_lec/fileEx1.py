fobj = open('hello.txt', 'w') #hello.txt 라는 파일을 만들어서 w = write mode 로 지정해줌
fobj.write('hello python file~~~~~') #write() 를통해서 그안에 넣어줄내용을 적어줌 
fobj.close() #파일 닫아주기 !필수!

fobj2 = open('hello.txt', 'r') #hello.txt 파일을 열라고 정해주고 r = read only 로 지정해줌
readStr = fobj2.read() #readStr 변수안에 파일을읽고 그내용을 그대로 넣어줌
print(readStr) #hello python file~~~~~
print(type(readStr)) #<class 'str'>
fobj2.close() #파일닫아주기 !필수!