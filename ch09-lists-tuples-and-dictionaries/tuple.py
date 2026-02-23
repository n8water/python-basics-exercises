# Tuple literal
# is a tuple that is written out explicitly as a comma-separated list of values 
# sourrounded by parantheses.

my_first_tuple = (1, 2, 3)
print(type(my_first_tuple))

mixed_tuple = (1, 2.0, "three")
print(type(mixed_tuple))

empty_tuple = ()
print(type(empty_tuple))

# create tuple with exactly one element
x = (1)
print(type(x))

# add a comma after the only element
x = (1,)
print(type(x))

# Built-in tuple()
# you can use the built-in tuple() to create a tuple from another sequence type, such as a string:
print(tuple("Python"))

# test
print(tuple(range(1, 5)))

vowels = ("a", "e", "i", "o", "u")

for vowel in vowels:
    print(vowel.upper())

# Tuple unpacking
# third but less common way of creating a tuple

coordinates = 4.21, 9.29
print(type(coordinates))
print(coordinates)

x, y = coordinates
print(f"x = {x}")
print(f"y = {y}")

# multiple variable assignemnts in a single line
# NOTE: Assigning more than two or three variables this way can make it
# difficult to tell which value is assigned to which variable name!
name, age, occupation = "Adisa", 34, "programmer"
print(name)
print(age)
print(occupation)

# The number of names and the number of values must be equal

try:
    a, b, c, d = 1, 2, 3
except ValueError:
    print("ValueError exception occured: ", ValueError.__doc__)

try:
    a, b, c = 1, 2, 3, 4
except ValueError:
    print("ValueError exception occured: ", ValueError.__doc__)

# checking the existence of values with 'in'

o_result = "o" in vowels
print("o in vowels?", o_result)

x_result = "x" in vowels
print("x in vowels?", x_result)

# Returning multiple values from a function

def adder_substractor(num1, num2):
    ''' Returns a tuple in which the first element is the sum of the two numbers
    and the second element is the difference between the two numbers'''
    return (num1 + num2, num1 - num2)

a = 3
b = 2

print(adder_substractor(a, b))

a = 4
b = 8
print(adder_substractor(a, b))

a = 0
print(adder_substractor(a, b))

# review exercises

"""
1. Create a tuple literal named cardinal_numbers that holds the strings
"first", "second", and "third", in that order.
2. Using index notation and print(), display the string at index 1 in
cardinal_numbers.
3. In a single line of code, unpack the values in cardinal_numbers into
three new strings named position1, position2, and position3. Then
print each value on a separate line.
4. Using tuple() and a string literal, create a tuple called my_name that
contains the letters of your name.
5. Check whether the character "x" is in my_name using the in keyword.
6. Create a new tuple containing all but the first letter in my_name using
slice notation.
"""

# 1
cardinal_numbers = ("first", "second", "third")

# 2
print(cardinal_numbers[1])

# 3
position1, position2, position3 = cardinal_numbers

print(position1)
print(position2)
print(position3)

# 4
my_name = tuple("Sabrina")

# 5 
contains_x = "x" in my_name
print("x in my_name?")
print(contains_x)

# or short
print("x" in my_name)

#6
sliced_tuple = my_name[1:]
print(sliced_tuple)

# or shorthand
print(my_name[1:])