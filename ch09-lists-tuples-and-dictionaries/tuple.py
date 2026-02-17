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