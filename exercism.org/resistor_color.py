""" Resistor en- and decoding of colours """

def color_code(color):
    """ Return int for color given"""
    if color in colors():
        return colors().index(color)
    return None

def colors():
    """ Colors definition """
    colors_list = [
        "black", 
        "brown", 
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "violet",
        "grey",
        "white"
    ]
    return colors_list

print(colors())
print(color_code("black"))
print(color_code("blue"))
print(color_code("pink"))