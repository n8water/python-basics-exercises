# Starting with lists, the first mutable squence we encounter

colors = ["red", "yellow", "green", "blue"]
print(type(colors))

print(colors)

# a list can consist of elements of different datatypes
sample_list = [ 1, 2.0, "three"]
print(type(sample_list))
print(sample_list)

# create a list using the built-in list()
# create a list from a tuple

print(list((1, 2, 4,)))

# create a list from a string
print(list("Python"))

# create a list from a string using split()
groceries = "eggs, milk, cheese, chocolate"
grocery_list = groceries.split(", ")
print(grocery_list)

# The string argument passed to .split() is called the separator
# by changing the separator, you can split strings into lists in
# numerous ways:

# split string on semicolon
print("a;b;c".split(";"))

# split string on spaces
print("The quick brown fox".split(" "))

# split string on multiple characters
# .split() always returns a list whose length is one more than the number
# of separators contained in the string. The separator "ba" appears twice,
# so the list returned by split() has three elements.
print("abbaabba".split("ba"))

# it the separator is not contained in the string at all, then .split()
# returns a list with the string as its only element
print("abbaabba".split("c"))

"""
In all, you’ve seen three ways to create a list:
1. A list literal
2. The built-in list()
3. The string .split() method
"""
