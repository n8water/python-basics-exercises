import random

# For example, unfair_coin_flip(.7) has a 70 percent chance of returning 'tails'
def unfair_coin_flip(probability_of_tails):
    ''' Randomly returns 'heads' or 'tails' with a given probability 0.x of returning 'tails' '''
    if random.random() < probability_of_tails:
       return 'tails'
    else:
        return 'heads'

heads_tally = 0
tails_tally = 0

for trial in range(10_000):
    if unfair_coin_flip(.7) == "heads":
        heads_tally = heads_tally + 1
    else:
        tails_tally += 1

ratio = heads_tally / tails_tally
print(f"The ratio of heads to tails is {ratio}")
    
heads_tally = 0
tails_tally = 0

for trial in range(10_000):
    if unfair_coin_flip(.4) == "heads":
        heads_tally += 1
    else:
        tails_tally += 1

ratio = heads_tally / tails_tally
print(f"The ratio of heads to tails is {ratio}")
