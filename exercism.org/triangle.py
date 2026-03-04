""" Triangle module """
def equilateral(sides):
    """ Check if a triangle is equilateral and returns 'True' or 'False' """
    if not sides_len_okay(sides):
        return False

    side1, side2, side3 = sides

    if side1 == side2 == side3:
        return True

    return False

def isosceles(sides):
    """ Check if a triangle is isosceles and returns 'True' or 'False' """
    if not sides_len_okay(sides):
        return False

    if not is_triangle(sides):
        return False

    side1, side2, side3 = sides

    if side1 == side2 or side1 == side3 or side2 == side3:
        return True
    return False

def scalene(sides):
    """ Check if a triangle is scalene and returns 'True' or 'False' """
    if not sides_len_okay(sides):
        return False

    if not is_triangle(sides):
        return False
            
    side1, side2, side3 = sides

    if side1 == side2 == side3:
        return False
    if side1 == side2 or side1 == side3 or side2 == side3:
        return False
    return True

def sides_len_okay(sides):
    """ Check input sides to be longer than '0' """
    return all(side > 0 for side in sides) # complex but shorter than for with if nested

def is_triangle(sides):
    """ Check if input can be a triangle """
    side1, side2, side3 = sides

    conditions_met = 0
    
    if side1 + side2 >= side3:
        conditions_met += 1
    if side2 + side3 >= side1:
        conditions_met += 1
    if side1 + side3 >= side2:
        conditions_met += 1
    return conditions_met == 3