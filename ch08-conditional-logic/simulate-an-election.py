import random

'''
With some help from the random module and a little conditional logic,
you can simulate an election between two candidates.
Suppose two candidates, Candidate A and Candidate B, are running
for mayor in a city with three voting regions. The most recent polls
show that Candidate A has the following chances for winning in each
region:
• Region 1: 87 percent chance of winning
• Region 2: 65 percent chance of winning
• Region 3: 17 percent chance of winning
Write a program that simulates the election ten thousand times and
prints the percentage of times in which Candidate A wins.
To keep things simple, assume that a candidate wins the election if
they win in at least two of the three regions
'''

region1_chance = 0.87
region2_chance = 0.65
region3_chance = 0.17

simulation_runs = 10_000
candidate_a_win_count = 0

def election(chance_candidate_a_wins):
    """ Randomly returns 'True' or 'False' depending on the result """
    if random.random() <= chance_candidate_a_wins:
        return True
    else:
        return False

for election_run in range(simulation_runs):
    region1_result = election(region1_chance)
    region2_result = election(region2_chance)
    region3_result = election(region3_chance)

    if (region1_result and region2_result) or (region1_result and region3_result) or (region2_result and region3_result):
        candidate_a_win_count +=1

candidate_a_win_quote = candidate_a_win_count / simulation_runs * 100

print(f"Candidate A wins in {candidate_a_win_quote: .2f} percent of simulations")

