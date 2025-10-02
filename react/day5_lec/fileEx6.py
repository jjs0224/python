import pickle

# file = open('obj_data.p', 'wb')

# name = 'kim'
# age = 20
# address = 'seoul'
# scores = {'korean':90, 'english':88, 'math':77}

# pickle.dump(name, file)
# pickle.dump(age, file)
# pickle.dump(address, file)
# pickle.dump(scores, file)
# file.close()

infile = open('obj_data.p', 'rb') #읽어올때 저장된순서로 읽어들여야함.. name, age, address, scores 순으로
name = pickle.load(infile)
age = pickle.load(infile)
address = pickle.load(infile)
scores = pickle.load(infile)
print(name, age, address) #kim 20 seoul
print(scores) #{'korean': 90, 'english': 88, 'math': 77}