'''
1. Write a program that prompts the user to enter a word using the
input() function and compares the length of the word to the num-
ber five. The program should display one of the following outputs,
depending on the length of the user’s input:
• "Your input is less than 5 characters long"
• "Your input is greater than 5 characters long"
• "Your input is 5 characters long"
'''

goal = 5
user_input = input("Enter a word: ")
input_len = len(user_input)


if input_len < goal:
    print(f"Your input is less than {goal} characters long")
elif input_len > goal:
    print(f"Your input is greater than {goal} characters long")
else:
    print(f"Your input is {goal} characters long")


'''
2. Write a program that displays "I'm thinking of a number between 1
and 10. Guess which one." Then use input() to get a number from
the user. If the user inputs the number 3, then the program should
display "You win!" For any other input, the program should display
"You lose."
'''

num = 3
print("\nI'm thinking of a number between 1 and 10. Guess which one.")
user_guess = int(input("What's your guess? "))

if user_guess == num:
    print("You win!")
else:
    print("You lose.")
