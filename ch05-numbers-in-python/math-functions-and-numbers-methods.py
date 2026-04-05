print(round(2.3))

print(round(2.7))


print(round(2.5))
print(round(3.5))
print(round(4.5))

# round with positions after the comma
print(round(2.74653, 3))


# skip abs() for absolute ValueError

# skip pow which is like **

# review exercises

'''
Write a program that asks the user to input a number and then
displays that number rounded to two decimal places. When run,
your program should look like this:
'''

prompt = "Enter a number: "
user_input = input(prompt)
print(f"{user_input} rounded to 2 decimal places is {round(float(user_input), 2)}")

'''
Write a program that asks the user to input a number and then
displays the absolute value of that number. When run, your
program should look like this:
'''

user_input = input(prompt)
print("The absolute value of " + user_input + " is " + str(abs(float(user_input))))

'''
Write a program that asks the user to input two numbers by using
input() twice, then displays whether the difference between those
two numbers is an integer. When run, your program should look
like this:
'''

prompt1 = "Enter a number: "
prompt2 = "Enter another number: "

user_input1 = input(prompt1)
user_input2 = input(prompt2)

print("The difference between {} and {} is an integer? {}".format(user_input1, user_input2, (float(user_input1) - float(user_input2)).is_integer()))
