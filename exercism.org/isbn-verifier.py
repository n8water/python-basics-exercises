""" Module to check if a given isbn is a valid isbn10 code """
def is_valid(isbn):
    """ Returns 'True' or 'False' after checking isbn to be a valid isbn-10 code """
    isbn_to_check = isbn.replace("-", "")
    isbn_to_check = isbn_to_check.strip()

    if not len(isbn_to_check) == 10:
        return False
    return True

print(is_valid("3-598-21508-8"))
print(is_valid(" 3-598-21508-8"))
print(is_valid("3-598-2108-8"))
print(is_valid("a-bdd-efghi-j"))