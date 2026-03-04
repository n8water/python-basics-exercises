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
        if str(word).startswith(rule1):
            translated_words.append(word + "ay")
            continue
        
        not_vowel = True
        translated_word = word

        for char in translated_word:
            if char in vowels:
                not_vowel = False
                break
            


            translated_words.append()
    
    result = ""
    for translation in translated_words:
        result = result + " " + translation

    return result


print(translate("apple xray yttria"))