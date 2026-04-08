"""
You have one hundred cats.
One day, you decide to arrange all your cats in a giant circle. Initially,
none of your cats has a hat on. You walk around the circle a hundred
times, always starting with the first cat (cat #1). Each time you stop at
a cat, you check if it has a hat on. If it doesn’t, then you put a hat on
it. If it does, then you take the hat off.
1. The first round, you stop at every cat, placing a hat on each one.
2. The second round, you stop only at every second cat (#2, #4, #6,
#8, and so on).
3. The third round, you stop only at every third cat (#3, #6, #9, #12,
and so on).
4. You continue this process until you’ve made one hundred rounds
around the cats. On the last round, you stop only at cat #100.
Write a program that simply outputs which cats have hats at the end.
"""

def get_cats(number_of_cats):
    ''' Create list of cats '''
    cats = []
    for c in range(number_of_cats):
        cats.append(False)
    return cats

#cats = get_cats(100)

my_cats = {}
cats_with_hats = []

# Create cats dict
for i in range(1,101):
    my_cats[i] = {"has_hat":False }
    
# rounds to go
for round in range(1, 101):
    for key, item in my_cats.items():
        if key % round == 0:
            # invert value of has_hat    
            item["has_hat"] = not item["has_hat"]

for key, item in my_cats.items():
    if item["has_hat"]:
        cats_with_hats.append(key)

print(cats_with_hats)