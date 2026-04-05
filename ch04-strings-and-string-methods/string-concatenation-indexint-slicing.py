# Concatenation
string1 = "abra"
string2 = "cadabra"
magic_string = string1 + string2
print(magic_string)

first_name = "Arthur"
last_name = "Dent"
full_name = first_name + " " + last_name
print(full_name)

# Indexing
flavor = "fig pie"
print("Get character at index 1 of " + flavor )
print(flavor[1])

# get last character
print("Get last charakter")
print(flavor[-1])

# substring
flavor_substring = flavor[0:3]
print("Substring 0:3 of flavor")
print(flavor_substring)

# substring from 3 till end
flavor_end = flavor[3:]
print(flavor_end)

# no IndexError if I try to slice between boundaries outside the beginning or
# ending of a string
print("End of substring is outside the index range")
print(flavor[:14])

print("Start and End are outside the strings lenght")
print(flavor[13:15])

# strings are immutable meaning characters cannot be changed
# changes require new string assignments
word = "goal"
print("Initial word " + word)
word = "f" + word[1:]
print("Result after concatenation of f plus word[1:]")
print(word)

# exercise
test = "bazinga"
print(test[2:6])
