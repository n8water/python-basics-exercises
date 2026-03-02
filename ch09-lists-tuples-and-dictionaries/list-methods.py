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
