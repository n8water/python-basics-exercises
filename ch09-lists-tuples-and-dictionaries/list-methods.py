# list.insert() takes an index i and a value x and inserts the value x at
# index i in the list:

colors = ["red", "yellow", "green", "blue"]
print("Original list")
print(colors)

# insert "orange" into the second position
colors.insert(1, "orange")
print('After colors.insert(1, "orange")')
print(colors)

# if value for index parameter of .insert() is larger than the greates index
# in the list, then the value is inserted at the end of the list:
colors.insert(10, "violet")
print("after colors.insert(10, 'violet')")
print(colors)


# You can also use negative indices with .insert()
# i = -1 inserts the value x to the currently last index.
# which results in moving the existing last value to the right. staying last
colors.insert(-1, "indigo")
print('After colors.insert(-1, "indigo")')
print(colors)


# Remove value from specified index list.pop() takes one parameter, an index i
# the value that is removed is returned by the method
color = colors.pop(3)
print("colors.pop(3) returned and removed: " + (color))

print("colors List after using colors.pop(3)")
print(colors)

# remove the last object from the list with pop(-1)
# .pop() without a value removes the last item in the list:
color = colors.pop(-1)
print("colors.pop(-1) returned and removed: " + (color))

print("colors List after using colors.pop(-1)")
print(colors)

# list.append()
# calling .appen() increases the length of the list by one and inserts the value into the final slot.
colors.append("pink")
print(colors)

# alternative way to add 'pink' to the end of the list
colors.pop()
print(colors)

colors.insert(len(colors), "pink")
print(colors)

# list.extend() method is used to add several new elements to the end of a list
colors.extend(["violet", "grey", "amber"])
print(colors)

# excurse to list-of-numbers.py

# List comprehensions
print("Create a tuple of numbers:")
my_numbers = (1, 2, 3, 4, 5)
print(my_numbers)
print("use list comprehensions")
print("squares = [num**2 for num in my_numbers]")
squares = [num**2 for num in my_numbers]
print("Result:")
print(squares)

# list comprehensions are commonly used to convert values in a list to a different type
print("\nList Comprehensions")
print("From string input to floats using list comprehension")
str_numbers = ["1.5", "2.3", "5.25"]
print(str_numbers)
print("float_numbers = [float(value) for value in str_numbers]")
float_numbers = [float(value) for value in str_numbers]
print(float_numbers)