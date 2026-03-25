try:
    number = int(input("Enter an integer: "))
except ValueError:
    print("That was not an integer")

print(number)


# multiple exception
def divide(num1, num2):
    try:
        print(num1 / num2)
    except (TypeError, ZeroDivisionError):
        print("encountered a problem")


divide(3, 6)
divide(4, 0)
divide(6, 's')


def divide2(num1, num2):
    try:
        print(num1 / num2)
    except TypeError:
        print("Both arguments must be numbers")
    except ZeroDivisionError:
        print("num2 must not be 0")

divide2(3, 6)
divide2(4, 0)
divide2(6, 's')

# review exercises

'''
1. Write a program that repeatedly asks the user to input an integer.
If the user enters something other than an integer, then the
program should catch the ValueError and display the message "Try
again."
Once the user enters an integer, the program should display
the number back to the user and end without crashing.
'''

keep_running = True

while(keep_running):
    try:
        num = int(input("Enter an integer: "))
    except ValueError:
        print("Try again")
        continue
    keep_running = False

print(num)


'''
2. Write a program that asks the user to input a string and an integer
n, then displays the character at index n in the string.
Use error handling to make sure the program doesn’t crash
if the user enters something other than an integer or if the index
is out of bounds. The program should display a different message
depending on which error occurs.
'''


