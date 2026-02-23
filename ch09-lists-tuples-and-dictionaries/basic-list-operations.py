# indexing and slicing
numbers = [1, 2, 3, 4]
print(f"The original numbers list: {numbers}")
print("Next the output of numbers[1]:")
print(numbers[1])

new_numbers = numbers[1:3]
print(f"The new list from the original list using slice notation 'numbers[1:3]'")
print(new_numbers)

# like in tuples we can use 'in' to check for the existence of list elements
# Check existence of an element
print("Test for 'Bob' in numbers")
print("Bob" in numbers)

# personal test how to handle numbers within in check
print(3 in numbers)

# iterate lists, print only even numbers
print("Lists are iterable. Print only the even number from the list")
for number in numbers:
    if number % 2 == 0:
        print(number)