""" Module to check for collatz conjecture """

def steps(number):
    """ Calculate how many steps it takes to reach 1 using Collatz Conjecture """
    if number < 0:
        raise ValueError("Only positive integers are allowed.")
        return
    if number == 0:
        raise ValueError("0 is an invalid input.")
        return

    current_value = number
    count = 0

    while current_value > 1:
        if current_value % 2 == 0:
            current_value = current_value / 2
        else:
            current_value = current_value * 3 + 1
        count += 1

    return count

print(steps(2))
print(steps(21))
print(steps(52))

try:
    result = steps(-2)
    print(result)
except ValueError:
    print("ValueError occured")

try:    
    print(steps(0))
except:
    print("Except hit")

print("Done")
