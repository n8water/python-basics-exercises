""" Isogram checker """
def is_isogram(string):
    """ Checks if a given string is an isogram and returns 'True' or 'False' """
    letters = []    
    string = string.lower()
    
    for letter in string:
        if not letter.isalpha():
            continue
        if letter not in letters:
            letters.append(letter)
            continue
        return False
    return True

# testing function above
word1 = "lumberjack"
word2 = "isograms"
word3 = "six-year-old"
word4 = "Alphabet"

words = [word1, word2, word3, word4]

for word in words:
    print(f"Is {word} an isogram?")
    print(is_isogram(word))
