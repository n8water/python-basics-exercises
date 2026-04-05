# converting string case

name1 = "Jean-Luc Picard".lower()
print(name1)

name2 = "Jean-Luc Picard"
print(name2.lower())

print(name1.upper())

print("Length of the variable ")
print(len(name1))

'''
Remove whitespace three string methods
.rstrip()
.lstrip()
.strip()
'''

name1 = """Jean-Luc Picard       """
print("Input with whitespace")
print(name1)
print(len(name1))

print("\nInput without whitespace")
print(name1.rstrip())
print(len(name1.rstrip()))




name1 = """     Jean-Luc Picard"""
print("Input with whitespace")
print(name1)
print(len(name1))

print("\nInput without whitespace")
print(name1.lstrip())
print(len(name1.lstrip()))


name1 = """     Jean-Luc Picard       """
print("Input with whitespace")
print(name1)
print(len(name1))

print("\nInput without whitespace")
print(name1.strip())
print(len(name1.strip()))

'''
.startswith()
.endswith()
'''
print("\nstartswith and endswith")
starship = "Enterprise"
print("Does starship '" + starship + "' start with 'en'?")
print(starship.startswith("en"))

print("Does starship '" + starship + "' start with 'En'?")
print(starship.startswith("En"))

print("Does starship '" + starship + "' end with 'risE'?")
print(starship.endswith("risE"))


print("""\nUpper and lower do not change the string.
    The return a copy""")
      

name = "Picard"
print(name.upper())
print(name)

print("To keep the change you need to assign it to the variable")
name = name.upper()
print("Result after name = name.upper()")
print(name)



# exercise

print("Animal".lower())
print("Badger".lower())
bee = "Honey Bee"
print(bee.lower())
print("Honey Badger".lower())

animal = "Animal"
badger = "Badger"
bee = "Honey Bee"
honey_badger = "Honey Badger"
print(animal.upper())
print(badger.upper())
print(bee.upper())
print(honey_badger.upper())


# exercise remove whitespace

string1 = " Filet Mignon"
string2 = "Brisket "
string3 = " Cheeseburger "

string1 = string1.lstrip()
string2 = string2.rstrip()
string3 = string3.strip()

print(string1)
print(string2)
print(string3)

startwith_string1 = "Becomes"
startwith_string2 = "becomes"
startwith_string3 = "BEAR"
startwith_string4 = "    bEautiful"

print(startwith_string1.startswith("be"))
print(startwith_string2.startswith("be"))
print(startwith_string3.startswith("be"))
print(startwith_string4.startswith("be"))

startwith_string1 = startwith_string1.lower()
startwith_string3 = startwith_string3.lower()
startwith_string4 = startwith_string4.lstrip().lower()

print(startwith_string1.startswith("be"))
print(startwith_string2.startswith("be"))
print(startwith_string3.startswith("be"))
print(startwith_string4.startswith("be"))

