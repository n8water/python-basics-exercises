'''
Docstring for ch08-conditional-logic.review-exercises

1. Write a function called roll() that uses randint() to simulate rolling
a fair die by returning a random integer between 1 and 6.

2. Write a program that simulates ten thousand rolls of a fair die and
displays the average number rolled.
'''

# exercise 1

import random

def roll():
    ''' randomly returns an integer between 1 and 6, inclusive '''
    return random.randint(1,6)

dice = roll()
print(dice)

# exercise 2

sum_of_rolls = 0

for trial in range(10_000):
    sum_of_rolls += roll()

average = sum_of_rolls / 10000
print(f"The average number rolled is {average}")