"""
Rule 1

If a word begins with a vowel, or starts with "xr" or "yt", add an "ay" sound to the end of the word.

For example:

    "apple" -> "appleay" (starts with vowel)
    "xray" -> "xrayay" (starts with "xr")
    "yttria" -> "yttriaay" (starts with "yt")

Rule 2

If a word begins with one or more consonants, first move those consonants to the end of the word and then add an "ay" sound to the end of the word.

For example:

    "pig" -> "igp" -> "igpay" (starts with single consonant)
    "chair" -> "airch" -> "airchay" (starts with multiple consonants)
    "thrush" -> "ushthr" -> "ushthray" (starts with multiple consonants)

Rule 3

If a word starts with zero or more consonants followed by "qu", first move those consonants (if any) and the "qu" part to the end of the word, and then add an "ay" sound to the end of the word.

For example:

    "quick" -> "ickqu" -> "ickquay" (starts with "qu", no preceding consonants)
    "square" -> "aresqu" -> "aresquay" (starts with one consonant followed by "qu")

Rule 4

If a word starts with one or more consonants followed by "y", first move the consonants preceding the "y"to the end of the word, and then add an "ay" sound to the end of the word.

Some examples:

    "my" -> "ym" -> "ymay" (starts with single consonant followed by "y")
    "rhythm" -> "ythmrh" -> "ythmrhay" (starts with multiple consonants followed by "y")

"""

""" Pig latin module """
def translate(text):
    """ Translate input to pig latin text """
    vowels = ("a", "e", "i", "o", "u")
    rule1 = ("a", "e", "i", "o", "u", "xr", "yt")
            
    text_as_list = text.split(" ")
    translated_words = []
    
    for word in text_as_list:
        translated_word = word
        consonants = ""
                
        for char in translated_word:
            if char in vowels:        
                break
            consonants = consonants + char

        if word.startswith(rule1):
            translated_words.append(word)
        elif "qu" in word:
            position_of_qu = word.find("qu")
            if position_of_qu >= 2:
                slice_of_word = word[:len(consonants)]
                rest_of_word = word[len(consonants):]
                if rest_of_word.startswith(vowels):
                    translated_word = rest_of_word + slice_of_word
                    translated_words.append(translated_word)                    
            elif word.find("qu") >= 0:
                translated_word = word[2 + position_of_qu:] + word[: 2 + position_of_qu]
                translated_words.append(translated_word)                
        else:
            if "y" in consonants:
                position_of_y = consonants.find("y")
                if position_of_y == 0:
                    translated_word = word[position_of_y + 1:] + word[:position_of_y + 1]
                    translated_words.append(translated_word)
                    continue
                translated_word = word[position_of_y:] + word[:position_of_y]
                translated_words.append(translated_word)
                continue
            
            translated_word = word[len(consonants):] + consonants
            translated_words.append(translated_word)            

    result = ""
    
    for translation in translated_words:
        result = result + " " + translation + "ay"

    return result.strip()


print(translate("apple"))
print(translate("queen"))
print(translate("square"))
print(translate("pig"))
print(translate("chair"))
print(translate("my"))
print(translate("rhythm"))
print(translate("liquid"))
print(translate("yellow"))