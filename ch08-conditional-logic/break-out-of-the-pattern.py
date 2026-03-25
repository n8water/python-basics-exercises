
print("Example using 'break'")
for n in range(4):
    if n == 2:
        break
    print(n)

print(f"Finished with n = {n}\n")

print("Example using 'continue'")
for i in range(4):
    if i == 2:
        continue
    print(i)

print(f"Finished with i = {i}")

# for ... else loop

user_phrase = input("Enter a phrase to evaluate: ")

for character in user_phrase:
    if character == "X":
        break
else:
    print("There was no 'X' in the phrase")

print("Final statement")

# practical example for a 'for ... else' loop

for n in range(3):
    password = input("Password: ")
    if password == "I<3Bieber":
        break
    print("Password is incorrect.")
else:
    print("Suspicious activity. The authorities have been alerted.")


# review exercises

'''
1. Using break, write a program that repeatedly asks the user for some
input and quits only if the user enters "q" or "Q".
'''

escape = 'q'
prompt = "Please enter some text: "
user_input = ""

while True: 
    user_input = input(prompt).lower()
    if user_input == escape:
        break

print("You did escape")

'''
2. Using continue, write a program that loops over the numbers 1 to
50 and prints all numbers that are not multiples of 3.
'''

print("\nHere are the number from 1 to 50 except the multiples of 3")

for num in range(1,51):
    if num % 3 == 0:
        continue
    print(num)
