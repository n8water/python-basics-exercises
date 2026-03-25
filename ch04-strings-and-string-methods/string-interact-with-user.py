# get input

input()

prompt = "Hey, what's up? "
user_input = input(prompt)
print("You said: " + user_input)


# do something with the user input

response = input("What should I shout? ")
shouted_response = response.upper()
print("Well, if you insist..." + shouted_response)


# exercise
question = "What is your favourite colour? "
answer = input(question)
print(answer)

answer_lower = input(question).lower()
print(answer_lower)

print("Number of characters in your favorite colour is: ")
print(len(answer_lower))


