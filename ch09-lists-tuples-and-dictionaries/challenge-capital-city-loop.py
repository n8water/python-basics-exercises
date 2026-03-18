""" Challenge Tuples, Lists, and Dictionaries (p269) """
import random
import capital

# my first try
# states = list(capital.capitals_dict.keys())
# random_state = random.choice(states)
# random_capital = capital.capitals_dict[random_state]

# sample solution
random_state, random_capital = random.choice(list(capital.capitals_dict.items()))

## my try
# guess = ""

# while guess.lower() != random_capital.lower():
#     guess = input(f"What is the capital of {random_state}?")
    
#     if guess.lower() == "exit":
#         print(random_capital)
#         print("Goodbye")
#         break

# if guess.lower() == random_capital.lower():
    # print("Correct")


# sample

while True:    
    guess = input(f"What is the capital of '{random_state}'? ").lower()
    if guess == "exit":
        print(f"The capital of '{random_state}' is '{random_capital}'.")
        print("Goodbye")
        break
    elif guess == random_capital.lower():
        print("Correct! Nice job.")
        break