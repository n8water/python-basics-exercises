x = "Hello, World"

def func():
    x = 2
    print(f"Inside 'func', x has the value {x}")

func()
print(f"Outside 'func', x has the value {x}")


# example of nested function explaining the scope of variables

x = 5

def outer_func():
    y = 3

    def inner_func():
        z = x + y
        return z

    return inner_func()

print(outer_func())

# global keyword

total = 0

def add_to_total(n):
    # without global total, total = ... would create a new assignment
    # cannot access a new assigned variable in assignment
    # global tells Python to look in the global scope for the name total
    # using global is considered bad form in general
    global total
    total = total + n

add_to_total(5)
print(total)


    
