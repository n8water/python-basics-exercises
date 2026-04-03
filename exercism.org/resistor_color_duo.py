""" Resistor color translator module """

COLORS = [
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

def value(colors):
    """ Return a two digit response for colors input"""
    result = ""

    for color in colors:
        if color in COLORS:
            if len(result) < 2:
                index = COLORS.index(color)
                result += str(index)
    
    return int(result)
    

print(value(["black", "green"]))
print(value(["brown", "black"]))
print(value(["brown", "green"]))
print(value(["black", "green", "yellow"]))