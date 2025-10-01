import pandas as pd

data = pd.DataFrame({'food':['bacon','pulled pork','bacon','pastrami','corned beef','bacon','pastrami','honey ham','nova lox'],
                    'ounces':[4,3,12,6,7.5,8,3,5,6]})
print(data)
print()

meat_animal = {
    'bacon':'pig',
    'pulled pork':'pig',
    'pastrami':'cow',
    'corned beef':'pig',
    'honey ham':'pig',
    'nova lox':'salmon'
}

print()
data['animal'] = data['food'].map(lambda x: meat_animal[x])
print(data)
print()
data['animal2'] = data['food'].map(meat_animal)
print(data)

