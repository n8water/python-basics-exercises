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
name, age, occupation = "Adisa", 34, "programmer"
print(name)
print(age)
print(occupation)