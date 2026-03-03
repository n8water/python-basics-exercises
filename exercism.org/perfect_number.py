""" Module to check numbers based on Nicomachus' classification """

def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    
    aliquot_sum = 0

    for num in range(1, number):
        if number % num == 0:
            aliquot_sum += num

    if aliquot_sum > number:
        return "abundant"
    if aliquot_sum < number:
        return "deficient"
    return "perfect"

print(classify(6))
print(classify(12))
print(classify(24))
print(classify(8))