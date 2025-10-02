#-------세트에 값1개추가하기(add()) , 세트에 객체추가하기(update())

sd1 = {1,2,3,4}
sd1.add(5) #추가시켜줄값이 하나일때만 사용가능...그리고 set 이기때문에 같은수면 추가가안됨
print(sd1) #{1, 2, 3, 4, 5}
#sd1.update(6)
#print(sd1) #TypeError: 'int' object is not iterable

sd1.update({7,8,9,10}) #객ㅊㅔ생성해서 추가해줌
print(sd1) #{1, 2, 3, 4, 5, 7, 8, 9, 10}
sd1.update([11,12,13,14]) #리스트도 객체로만들어서 추가해줌
print(sd1) #{1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14}
sd1.update((15,16,17)) #Tuple 도 추가가능
print(sd1) #{1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17}
 
#---현재 세트가 다른세트와 겹치지않는지 확인(isdisjoint) 겹치는게없어?물어봄---
sd3 = {1,2,3,4}
sd4 = {5,6,7,8}
print(sd3.isdisjoint(sd4)) #True 겹치는요소가 없음
sd5 = {3,4,5,6}
print(sd3.isdisjoint(sd5)) #False 겹침

#---comprehension way to initialize varible 
sd6 = {i for i in 'hello'}
print(sd6) #{'h', 'o', 'l', 'e'}

sd7 = {i for i in 'hello world' if i not in 'wl'}
print(sd7) #{'o', 'h', 'r', ' ', 'd', 'e'}
