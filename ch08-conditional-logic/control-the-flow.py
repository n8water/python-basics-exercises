div_line = 50 * '#'

print(f"\n{div_line}\nThe Start of sample 1\n{div_line}\n")

if 2 + 2 == 4:
    print("2 and 2 is 4")

if 2 + 2 == 5:
    print("Is this the mirror universe?")




# selective code execution on condition
# if keyword
print(f"\n{div_line}\nThe Start of 'if' sample\n{div_line}\n")

grade = 40

if grade >= 70:
    print("You passed the class!")

if grade < 70:
    print("You did not pass the class :( ")

print("Thank you for attending.")

# if - else keywords
print(f"\n{div_line}\nThe Start of 'if - else' sample\n{div_line}\n")

if grade >= 70:
    print("You passed the class!")
else:
    print("You did not pass the class :( ")

print("Thank you for attending.")

# elif keyword
print(f"\n{div_line}\nThe Start of 'elif' sample\n{div_line}\n")

grade = 85

if grade >= 90:
    print("You passed the class with an A.")
elif grade >= 80:
    print("You passed the class with an B.")
elif grade >= 70:
    print("You passed the class with a C.")
else:
    print("You did not pass the class :( ")

print("Thank you for attending")


# nested if statements
print(f"\n{div_line}\nThe Start of nested if statements sample\n{div_line}\n")

sport = input("Enter a sport: ")
p1_score = int(input("Enter player 1 score: "))
p2_score = int(input("Enter player 2 score: "))

# 1 basketball

if sport.lower() == "basketball":
    if p1_score == p2_score:
        print("The game is a draw.")
    elif p1_score > p2_score:
        print("Player 1 wins.")
    else:
        print("Player 2 wins.")

# 2 golf
elif sport.lower() == "golf":
    if p1_score == p2_score:
        print("The game is a draw.")
    elif p1_score < p2_score:
        print("Player 1 wins.")
    else:
        print("Player 2 wins.")

# 2 other sports
else:
    print("Unknown sport")


# refactor to reduce complexity

print(f"\n{div_line}\nThe Start of refactored nested if statements sample\n{div_line}\n")

sport = input("Enter a sport: ")
p1_score = int(input("Enter player 1 score: "))
p2_score = int(input("Enter player 2 score: "))

# same score is a draw regardless of the sport
if p1_score == p2_score:
    print("The game is a draw.")

elif sport.lower() == "basketball":
    if p1_score > p2_score:
        print("Player 1 wins.")
    else:
        print("Player 2 wins.")

# 2 golf
elif sport.lower() == "golf":
    if p1_score < p2_score:
        print("Player 1 wins.")
    else:
        print("Player 2 wins.")

# 2 other sports
else:
    print("Unknown sport")

# refactor to use compount conditional expressions:
print(f"\n{div_line}\nThe Start of refactored code using compound conditional\n" +
      f"expressions sample\n{div_line}\n")

sport = input("Enter a sport: ")
p1_score = int(input("Enter player 1 score: "))
p2_score = int(input("Enter player 2 score: "))

sport = sport.lower()

if p1_score == p2_score:
    print("The game is a draw")
elif (sport == "basketball") or (sport == "golf"):
    p1_wins_bball = (sport == "basketball") and (p1_score > p2_score)
    p1_wins_golf = (sport == "golf") and (p1_score < p2_score)
    p1_wins = p1_wins_bball or p1_wins_golf
    if p1_wins:
        print("Player 1 wins.")
    else:
        print("Player 2 wins.")
else:
    print("Unknown sport")
