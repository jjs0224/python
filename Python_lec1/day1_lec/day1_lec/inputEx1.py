
# idata = input('정수값을 입력하세요: ')
# result = idata + 100 //idata is str so typeError
# print(result)


idata = input('정수값을 입력하세요: ') #or int(input('정수값을 입력하세요))
print(type(idata))
result = int(idata) + 100
print(result)