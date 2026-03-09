# Nesting
two_by_two = [[1, 2], [3, 4]]

# two_by_two has length 2
print(len(two_by_two))

# both elements of two_by_two are lists
print(two_by_two[0])
print(two_by_two[1])

print("two_by_two[1]")
print(two_by_two[1])

print("two_by_two[1][0]")
print(two_by_two[1][0])
print()
# Copying

print("*" * 50)
animals = ["lion", "tiger", "frumious Bandersnatch"]
# shallow copy, copies the reference to the same object. 
# A variable name is really just a reference to a specific location in computer memory. 
large_cats = animals
large_cats.append("Tigger")

print("animals after large_cats = animals and large_cats.append('Tigger')")
print(animals)

# to get an independent kopy of the animals list, you can use slice notation to return a new list with
# the same values
animals = ["lion", "tiger", "frumious Bandersnatch"]
large_cats = animals[:]
large_cats.append("leopard")

print("large_cats created with slice notation animals[:] and after appending a new animal")
print(large_cats)

print("Animals to show it is not affected by changes to large_cats")
print(animals)

import copy
mamals = copy.deepcopy(animals)
print("New list created using copy.deepcopy(list)")
print(mamals)
print("Add new element to new list")
mamals.append("lynx")
print("Result after adding new animal to mamals")
print(mamals)
print("Animals list after editing the mamals list copy of animals")
print(animals)
print()
# Sorting
# .sort() sorts all items in ascending order. By default, the list is sorted in alphabetical or numerical order
# depending on the type of elements in the list

# list of strings are sorted alphabetically
print("*" * 50)
print('colors = ["red", "yellow", "green", "blue"]')
colors = ["red", "yellow", "green", "blue"]
colors.sort()
print(colors)
print()
# list of numbers are sorted numerically
numbers = [1, 10, 5, 3]
print("numbers = [1, 10, 5, 3]")
print(numbers)
print("numbers.sort()")
numbers.sort()
print(numbers)

# sort() has an optional parameter called key that can be used to adjust how the list gets sorted
print()
print("colors.sort(key=len)")
colors.sort(key=len)
print(colors)
print()
print("*" * 50)
# user-defined function to key
def get_second_element(item):
    """ Returns the second element of item passed in """
    return item[1]

items = [(4, 1), (1, 2), (-9, 0)]
print("Items before sorting")
print(items)
items.sort(key=get_second_element)
print("Items after sorting with user-defined 'get_second_element' as key")
print(items)

print()
print("*" * 50)

# Review Exercise

""" 
1. Create a tuple called data with two values. The first value should
be the tuple (1, 2), and the second value should be the tuple (3,
4).
"""
data = ((1, 2), (3, 4))
print(data)

"""
2. Write a for loop that loops over data and prints the sum of each
nested tuple. The output should look like this:
Row 1 sum: 3
Row 2 sum: 7
"""
counter = 1

for element in data:
    print(f"Row {counter} sum: {sum(element)}")
    counter += 1

"""
3. Create the list [4, 3, 2, 1] and assign it to the variable numbers.
"""
numbers = list(range(4,0,-1))
print(numbers)

"""
4. Create a copy of the numbers list using the [:] slice notation.
"""
copy_numbers = numbers[:]
print(copy_numbers)

"""
5. Sort the numbers list in numerical order using .sort()
"""
numbers.sort()
print(numbers)
print(copy_numbers)

another_copy = numbers[-1::-1]
print("An other copy")
print(another_copy)
