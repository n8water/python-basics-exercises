def is_armstrong_number(number):
    original_number = number
    numbers = []
    
    while number > 0:
        num = number % 10
        numbers.insert(0, num)
        number = number // 10

    numbers_count = len(numbers)
    numbers_sum = 0
    
    for member in numbers:
        numbers_sum += member ** numbers_count

    return numbers_sum == original_number

print(is_armstrong_number(5))
