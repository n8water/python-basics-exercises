""" Module to inform customers about their number in line of customers """
def line_up(name, number):
    """ Return a string telling customer rank in line """
    if number % 10 == 1 and not number % 100 == 11:            
        suffix = "st"
    elif number % 10 == 2 and not number % 100 == 12:
        suffix = "nd"
    elif number % 10 == 3 and not number % 100 == 13:
        suffix = "rd"
    else:
        suffix = "th"

    return f"{name}, you are the {number}{suffix} customer we serve today. Thank you!"
    

print(line_up("Mary", 1))
print(line_up("John", 12))
print(line_up("Dahir", 9))


