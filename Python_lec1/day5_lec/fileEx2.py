infile1 = open('data\FirstPresidents.txt', 'r')
# rstr = infile1.read()
# print(rstr)

# for line in infile1:
#     print(line, end='') 

ldata = [line for line in infile1]
print(ldata) #['George Washington\n', 'John Adams\n', 'Thomas Jefferson\n']

ldata = [line.rstrip() for line in infile1]
print(ldata) #['George Washington', 'John Adams', 'Thomas Jefferson']