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

# Copying

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


# Sorting