""" Module to cypher input text """
import string

def rotate(text, key):
    """ Encrypt input text using rotational cypher """
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    #print(f"len(lower) = {len(lower)}")
    result = ""
    
    for letter in text:
        if letter in lower:
            index = lower.find(letter)
            new_index = index + key
            if new_index >= len(lower):
                new_index -= 26
            elif new_index < 0:
                new_index += 26
            result += lower[new_index]
        elif letter in upper:                    
            index = upper.find(letter)
            new_index = index + key
            if new_index >= len(upper):
                new_index -= 26
            result += upper[new_index]
        else:
            result += letter

    return result


print(rotate("a", 1))
print(rotate("z", 1))
print(rotate("a", -1))
print(rotate("Cool", 12))
