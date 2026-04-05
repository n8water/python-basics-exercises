import random

def unfair_toss(probability_of_tails):
    if random.random() < probability_of_tails:
        return 'tails'
    else:
        return 'heads'


heads_tally = 0
tails_tally = 0

for trial in range(10_000):
    if unfair_toss(0.8) == 'heads':
        heads_tally += 1
    else:
        tails_tally += 1
        
ratio = heads_tally / tails_tally
print(f"The ration of heads to tail is {ratio}")