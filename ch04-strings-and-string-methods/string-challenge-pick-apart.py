'''4.5. Challenge: Pick Apart Your User’s Input
4.5 Challenge: Pick Apart Your User’s
Input
Write a program named first_letter.py that prompts the user for in-
put with the string "Tell me your password:". The program should then
determine the first letter of the user’s input, convert that letter to up-
percase, and display it back.
For example, if the user input is "no", then the program should display
the following output
The first letter you entered was: N'''

prompt = "Tell me your password: "
user_input = input(prompt)
print("The first letter you entered was: " + user_input[:1].upper())
