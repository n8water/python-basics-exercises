import random

def coin_flip():
    """Randomly return 'heads' or 'tails'"""
    if random.randint(0, 1) == 0:
        return 'heads'
    else:
        return 'tails'

# First initialize the taallies to 0
heads_tally = 0
tails_tally = 0

for trial in range(50_000):
    if coin_flip() == 'heads':
        heads_tally = heads_tally + 1
    else:
        tails_tally = tails_tally +1

ratio = heads_tally / tails_tally
print(f"The ratio of head to tails is {ratio}")
