import random

def dice():
    ''' Throw a dice and return the result'''
    result = random.randint(1, 6)
    print(result)
    return result

for num in range(0, 10):
    dice()
