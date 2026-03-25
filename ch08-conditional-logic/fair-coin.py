import random

def toss():
    if random.randint(0,1) == 0:
        return 'heads'
    else:
        return 'tails'

heads_tally = 0
tails_tally = 0

for trial in range(10_000):
    if toss() == 'heads':
        heads_tally = heads_tally + 1
    else:
        tails_tally = tails_tally + 1

ratio = heads_tally / tails_tally
print(f"The ratio is {ratio}")
