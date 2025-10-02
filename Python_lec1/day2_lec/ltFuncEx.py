# ldata1 = [90, 50, 40, 70, 10]
# for data in ldata1:
#     print(data)

# print()

# for data in enumerate(ldata1):  #tuple 로 받음
#     print(data)   #(0, 90)
#                   #(1, 50)
#                   #(2, 40)
#                   #(3, 70)
#                   #(4, 10)

# for index, ldata in enumerate(ldata1):
#     print(index, ldata)  #0 90
#                          #1 50
#                          #2 40
#                          #3 70
#                          #4 10

# for index, ldata in enumerate(ldata1, start=2): #set start index. i=start
#     print(index, ldata)  #2 90
#                          #3 50
#                          #4 40
#                          #5 70
#                          #6 10
                 
names = ['kim', 'lee', 'choi', 'hyo']
heights = [170, 180, 160, 190]
weights = [65, 90, 50, 110]

for i in range(len(names)):
    print('name:{} height:{} weight:{}'.format(names[i], heights[i], weights[i]))

for name, height, weight in zip(names, heights, weights): #같은 인덱스에 있는것들을 튜플로받음
    #print('name:', name, 'height:', height, 'weight:', weight)
    print(f'name:{name} height:{height} weight:{weight}')

