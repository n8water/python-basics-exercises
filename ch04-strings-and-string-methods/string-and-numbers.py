# convert input (string) to numer

num = input("Enter a number to be doubled: ")
doubled_num = num * 2
print(doubled_num)



num = input("Enter a number to be doubled: ")
doubled_num = int(num) * 2
print(doubled_num)


# Review exercises

num_string = "5"
num_int = int(num_string)
print("String to int and multiplied is " + num_string)
print(num_int *2)


num_float = float(num_string)
print("Float from string multiplied by 3.5")
print(num_float * 3.5)


# string and integer object in print statment

text = "Hello"
num = 42
print(text + " " + str(num))

# 2 inputs are calculated and written

print("Please enter two numbers to multiply")
prompt = "Number 1: "
input1 = input(prompt)
prompt = "Number 2: "
input2 = input(prompt)
result = float(input1) * float(input2)
print(result)
print("The product of " + input1 + " and " + input2 + " is " + str(result) + ".")

# streamline your prints

name = "Zaphod"
heads = 2
arms = 3

# starting from python 3.6
print(name + " has " + str(heads) + " heads and " + str(arms) + " arms.")

# earlier versions use .format()
print("{} has {} heads and {} arms.".format(name, heads, arms))


# formatted strings
print(f"{name} has {heads} heads and {arms} arms.")

n = 3
m = 4
print(f"{n} times {m} is {n*m}")


# Review exercise

weight = 0.2
animal = "newt"

print( str(weight) + " kg is the weight of the " + animal)

print("{} kg is the weight of the {}".format(weight, animal))

print(f"{weight} kg is the weight of the {animal}")
