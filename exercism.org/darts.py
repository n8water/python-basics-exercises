""" Calculate points scored in a single toss of a Darts game """

def score(x, y):
    """ Returns score as int depending on where the dart landed """
    target_radius = (x ** 2 + y ** 2) ** 0.5
    if target_radius <= 1:
        return 10
    if target_radius <= 5:
        return 5
    if target_radius <= 10:
        return 1
    return 0
