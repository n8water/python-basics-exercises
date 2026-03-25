def multiply(x, y): # function signature
    # function body
    '''Return the product of two numbers x and y.'''
    product = x * y
    return product
    print("Will never be reached, because of return before")

print("Outside the function")
print("Call multiply with the arguments of 2 and 3")
print(multiply(2, 3))

print(multiply("Hello ", 2))


def greet(name):
    print(f"Hello, {name}!")

my_value = greet("Sam")
print(my_value)
print(type(my_value))

# review exercises
'''1. Write a function called cube() that takes one number parameter
and returns the value of that number raised to the third power.
Test the function by calling your cube() function on a few different
numbers and displaying the results.
'''
def cube(x):
    '''Return the number provided x raised to the third power'''
    result = pow(x, 3)
    print(f"Result of cube({str(x)}) is {result}")
    return result

cube(2)
cube(3)
cube(99)
cube(-1.2)


'''
2. Write a function called greet() that takes one string parameter
called name and displays the text "Hello <name>!", where <name> is
replaced by the value of the name parameter.
'''

def greet(name):
    '''Display the text "Hello <name>!" where name is string given'''
    print(f"Hello {name}!")

greet("Sam")
greet("Willie")
greet("Everyone")


# Challenges

'''
1. convert_cel_to_far(), which takes one float parameter representing degrees
Celsius and returns a float representing the same temperature in degrees
Fahrenheit using the following formula:
F = C * 9/5 + 32
'''
def convert_cel_to_far(c):
    '''Take float parameter c representing degrees Celsius and return a
float representing the same temperature in degrees Fahrenheit'''
    far = c * 9/5 + 32
    return far

'''
2. convert_far_to_cel(), which takes one float parameter representing degrees Fahrenheit and returns a float representing the same
temperature in degrees Celsius using the following formula:
C = (F - 32) * 5/9
'''

def convert_far_to_cel(f):
    '''Take float parameter f representing degrees Fahrenheit and return a
a float representing the same temperature in degrees Celsius'''
    cel = (f - 32) * 5/9
    return cel

prompt_far = "Enter a temperature in degrees F: "
prompt_cel = "Enter a temperature in degrees C: "

far = input(prompt_far)
result_cel = convert_far_to_cel(float(far))
print(f"{far} degrees F = {result_cel:.2f} degrees C")

cel = input(prompt_cel)
result_far = convert_cel_to_far(float(cel))
print(f"{cel} degrees C = {result_far:.2f} degrees F")




