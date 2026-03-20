""" Module to check if a given isbn is a valid isbn10 code """
def is_valid(isbn):
    """ Returns 'True' or 'False' after checking isbn to be a valid isbn-10 code """
    isbn_to_check = isbn.replace("-", "")
    
    # check length a valid isbn has a length of 10 9 digits plus one check character
    if not len(isbn_to_check) == 10:
        return False

    # get check character
    check_charakter = isbn_to_check[-1]
    if check_charakter.lower() == "x":
        check_charakter = 10
    elif not check_charakter.isnumeric():
        return False

    # check if position 0-9 are digits
    if not isbn_to_check[:9].isnumeric():
        return False

    # check validity
    multiplicator = 10
    checksum = 0

    for number in isbn_to_check[:9]:
        checksum += int(number) * multiplicator
        multiplicator -= 1
    
    checksum += int(check_charakter)
    if checksum % 11 != 0:
        return False

    return True

print(is_valid("3-598-21508-8"))
print(is_valid(" 3-598-21508-8"))
print(is_valid("3-598-2108-8"))
print(is_valid("a-bdd-efghi-j"))
print(is_valid("3-598-21507-X"))