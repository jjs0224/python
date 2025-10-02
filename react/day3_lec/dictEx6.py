keys = ['a', 'b', 'c', 'd']
d1 = dict.fromkeys(keys) #set default values with None for all keys
print(d1) #{'a': None, 'b': None, 'c': None, 'd': None}

d2 = dict.fromkeys(keys, 100) #set default value for all keys with 100
print(d2) #{'a': 100, 'b': 100, 'c': 100, 'd': 100}

sentence = 'have a good day'
d3 = {index:word for index, word in enumerate(sentence.split())}
print(d3) #{0: 'have', 1: 'a', 2: 'good', 3: 'day'}

d3 = {index:[word, len(word)] for index, word in enumerate(sentence.split())}
print(d3) #{0: ['have', 4], 1: ['a', 1], 2: ['good', 4], 3: ['day', 3]}