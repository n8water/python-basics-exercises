import random

# better overview of lists if one element per line
nouns = [
    "fossil", 
    "horse", 
    "aardvark", 
    "judge", 
    "chef", 
    "mango", 
    "extrovert", 
    "gorilla"
    ]
verbs = [
    "kicks", 
    "jingles", 
    "bounces", 
    "slurps", 
    "meows", 
    "explodes", 
    "curdles"
    ]
adjectives = [
    "furry", 
    "balding", 
    "incredulous", 
    "fragrant", 
    "exuberant",
    "glistening"
    ]
prepositons = [
    "against", 
    "after", 
    "into", 
    "beneath", 
    "upon", 
    "for", 
    "in", 
    "like", 
    "over", 
    "within"
    ]
adverbs = [
    "curiously", 
    "extravagantly", 
    "tantalizingly", 
    "furiously", 
    "sensuously"
    ]

def get_random_elements(list, count):
    """ Function returns count number of random elements from the list """
    result = []
    for i in range(count):
        result.append(random.choice(list))
    return result

# sample how to use random.choice()
# random_element = random.choice(["a", "b", "c"])
# print(random_element)

noun_count = 3
verb_count = 3
adjective_count = 3
preposition_count = 2

# output structure
"""
{A/An} {adj1} {noun1}

{A/An} {adj1} {noun1} {verb1} {prep1} the {adj2} {noun2}
{adverb1}, the {noun1} {verb2}
the {noun2} {verb3} {prep2} a {adj3} {noun3}
"""

# # get random elements
# random_nouns = get_random_elements(nouns, noun_count)
# random_verbs = get_random_elements(verbs, verb_count)
# random_adjectives = get_random_elements(adjectives, adjective_count)
# random_prepositions = get_random_elements(prepositons, preposition_count)

# # split lists
# noun1, noun2, noun3 = random_nouns
# verb1, verb2, verb3 = random_verbs
# adj1, adj2, adj3 = random_adjectives
# prep1, prep2 = random_prepositions
# adverb1 = random.choice(adverbs)

# combine the get random elements with splitting the lists
noun1, noun2, noun3 = get_random_elements(nouns, noun_count)
verb1, verb2, verb3 = get_random_elements(verbs, verb_count)
adj1, adj2, adj3 = get_random_elements(adjectives, adjective_count)
prep1, prep2 = get_random_elements(prepositons, preposition_count)
adverb1 = random.choice(adverbs)

article = "A"
vowels = "aeiou"

if adj1[0] in vowels:
    article = "An"

# print output
print(f"""{article} {adj1} {noun1}

{article} {adj1} {noun1} {verb1} {prep1} the {adj2} {noun2}
{adverb1}, the {noun1} {verb2}
the {noun2} {verb3} {prep2} a {adj3} {noun3}""")

# I did not take into account, that random.choice might draft the same word 
# multiple times.
# the whole random and creation act could be in the new function.
# first try 17.03.2026
