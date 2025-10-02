# def number_generator():
#     yield 0
#     yield 1
#     yield 2

# for i in number_generator():
#     print(i)    #0 = 처음 number_generator() 불렀을때 yield 0 값을 리턴함, 그리고 대기상태(stopped after yield 0)
#                 #1 = 다시 포문에서 또 number_generator() 호출하면서 yield 1 을 리턴.. 그리고 대기상태
#                 #2 = 다시 호출하면서 yield 2 를 리턴.. 그리고 더이상 yield 가 없음으로 stopIteration 을 리턴함 == stops for loop

# print()
# g = number_generator()
# print(g) #<generator object number_generator at 0x0000021EDF9806D0>
# print(next(g)) #0
# print(next(g)) #1
# print(next(g)) #2
# print(next(g)) #StopIteration

# def number_generator2(stop):
#     n = 0
#     while n < stop:
#         yield n 
#         n += 1

# for i in number_generator2(4):
#     print(i)    #0
#                 #1
#                 #2
#                 #3

fruits = ['apple', 'pear', 'orange', 'banana']

def upper_generator(x):
    for data in x:
        yield data.upper()

for i in upper_generator(fruits):
    print(i)    #APPLE
                #PEAR
                #ORANGE
                #BANANA