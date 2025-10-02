iValue = 2423
fValue = 3323.645786

# makeStr = 'iValue: %d fValue: %f'%(iValue, fValue) #%d = int value %f = float value
# print(makeStr)
# print()

# makeStr2 = 'iValue:{0} fValue:{1}'.format(iValue, fValue)
# print(makeStr2)
# makeStr2 = 'iValue:{} fValue:{}'.format(iValue, fValue) #보통 순서대로 값을가져오기때문에 인덱스 안넣어줘도 사용가능
# print(makeStr2)

# makeStr = 'iValue: %10d fValue: %15f'%(iValue, fValue) #%10d = 값을가져올때 공간 10개로 세팅해줌   iValue:       2423 fValue:     3323.645786
# print(makeStr)

# makeStr = 'iValue: %-10d fValue: %-15f'%(iValue, fValue) #%-10d = minus 넣어주면 앞에서부터 정렬됨 iValue: 2423       fValue: 3323.645786
# print(makeStr)

# makeStr = 'iValue: %10d fValue: %15.2f'%(iValue, fValue) #%15.2f = decimal point to 2 . only for float value
# print(makeStr)

makeStr2 = 'iValue:{0:10} fValue:{1:15}'.format(iValue, fValue)
print(makeStr2)
makeStr2 = 'iValue:{:10} fValue:{:15}'.format(iValue, fValue)
print(makeStr2)
makeStr2 = 'iValue:{:<10} fValue:{:15}'.format(iValue, fValue) #iValue:2423       fValue:    3323.645786
print(makeStr2)
makeStr2 = 'iValue:{:10} fValue:{:15.2f}'.format(iValue, fValue) #iValue:      2423 fValue:        3.3e+03
print(makeStr2)

makeStr3 = f'iValue:{iValue:<10} fValue:{fValue:15.2f}'
print(makeStr3)