# use .find() which returns the index of the start of the substring

phrase = "the surprise is in here somewhere"
to_find = "surprise"
print("Looking for " + to_find)
print(phrase.find("surprise"))
to_find = "eyjafjallajökull"

# find() returns -1 if not found
print("Now looking for " + to_find)
print(phrase.find("eyjafjallajökull"))

# find() is casesensitve and all characters must match
print(phrase.find("SURPRISE"))

# find() returns only the start indext of the first occurance
msg = "I put a string in your string"
print(msg)
print(msg.find("string"))

# numbers in string
text = "My number is 555-555-5555"
print(text)
# will cause TypeError
# print("Find 5")
#print(text.find(5))
print("Find '5'")
print(text.find("5"))


# replace
my_story = "I'm telling you the truth; nothing but the truth!"
print("Original: " + my_story)
print("replaced: " + my_story.replace("the truth", "lies"))
print("Call variable again to see it unaltered: " + my_story)
my_story = my_story.replace("the truth", "lies")
print("Finally: " + my_story)

# to replace various words
sample = "some of the stuff"
print("Go from: " + sample)
new_sample = sample.replace("some of", "all")
new_sample = new_sample.replace("stuff", "things")
print("To: " + new_sample)

# Review exercises
print("AAA".find("a"))

exercise2 = "Somebody said something to Samantha."
result2 = exercise2.replace("s", "x")
print(result2)

exercise3 = "Please give me a word: "
input_from_user = input(exercise3)
print(input_from_user.find("b"))

