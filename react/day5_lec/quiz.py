x = input('대륙 이름을 입력하세요: ')

infile = open('data/UN.txt', 'r')
pdata = [line for line in infile]

for a in pdata:

    b = a.split(',')
   
    if x.lower() in b[1].lower():
        print(b[0]) 


    