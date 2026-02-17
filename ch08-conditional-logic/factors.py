'''
Write a program called factors.py that asks the user to input a posi-
tive integer and then prints out the factors of that number.
'''

user_input = int(input("Enter a positive integer: "))

for num in range(1, user_input + 1):
    if user_input % num == 0:
        print(f"{num} is a factor of {user_input}")


# did it! the wording in the sample solution is a bit different
