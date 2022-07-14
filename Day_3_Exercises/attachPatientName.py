import numpy.random as random

def attachNames(data, names:list):
    return[{'name':name, 'data':list(data)} for (name,data) in zip(names,data)]

data = random.randint(10, size=(3,5))
names=['Alice','Bob','Charlie']

print(attachNames(data,names))