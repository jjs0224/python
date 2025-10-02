with open('Both.txt','r', encoding='utf-8') as file: #이방식사용하면 file.close() 해줄필요없음
    rstr = file.read()
    
print(rstr)