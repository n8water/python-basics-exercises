# while loop
# perfect for repeating a section of code while some
# condition is met

num = float(input("Enter a positive number: "))

while(num <= 0):
    print("That's not a positive number!")
    num = float(input("Enter a positive number: "))

print("You did it!")

# for loop
# for repeating a section of code a specific number of times
# executes a section of code once for eacht item in a collection?
# sounds like a foreach in C#

for letter in "Python":
    print(letter)

print("\n")

# same as while loop
word = "Python"
index = 0

while index < len(word):
    print(word[index])
    index = index + 1

for n in range(3):
    print(n)
    print("Python")
    
# range can have a start and an end point, whereas the start is included
# while end is not
print("\nfor loop with a range of 10 to 20")
for n in range(10, 20):
    print(n * n)

# example to split an amount between a raising number of people
# 2, 3, 4 and 5
amount = float(input("Enter an amount: "))

for num_people in range(2, 6):
    print(f"{num_people} people: ${amount / num_people:,.2f} each")

# nested loops - loop inside a loop
print("\nNested loop sample:")
for n in range(1, 4):
    for j in range(4, 7):
        print(f"n = {n} and j = {j}")


# review exercise:

'''
1. Write a for loop that prints out the integers 2 through 10, each on
a new line, using range().
'''
for n in range(2, 11):
    print(n)

'''
2. Write a while loop that prints out the integers 2 through 10. (Hint:
You’ll need to create a new integer first.)
'''
count = 2

while count <= 10:
    print(count)
    count += 1


'''
3. Write a function called doubles() that takes a number as its input
and doubles it. Then use doubles() in a loop to double the number 2
three times, displaying each result on a separate line. Here’s some
sample output:
4
8
16
'''
def doubles(x):
    '''Takes a number and doubles it'''
    return x * 2

current_value = 2

for n in range(3):
    current_value = doubles(current_value)
    print(current_value)
