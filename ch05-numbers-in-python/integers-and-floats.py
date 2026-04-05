separator = "#"
separator_multiplier = 50

# integers
print(type(1))

# literal integers are type in
num = 23

# integers converted from strings are not called literal integers
text = "34"
num2 = int(text)
print(num2)

num1 = 1000000
# you can use underscores to group large integer to make them easier to read
num2 = 1_000_000

print(num1 - num2)

# integers do not have a limitation in phython
print(separator * separator_multiplier)

# floating point numbers
print(type(2.5))

print(float("2.33"))

# different ways of representing floating point numbers
a = 1000000.0
b = 1_000_000.0
# exponential notation
# number multiplied by 10 raised to the power of number after e
# 1 e 6 = 1 * 10^6
c = 1e6

print("Input: 1000000.0")
print(str(a))
print("Input: 1_000_000.0")
print(str(b))
print("Input: 1e6")
print(str(c))

# When you reach the maximum floating-point number, Python returns
# a special float value, inf == infinity


# Review exercises

num1 = 25_000_000.0
num2 = 25e6
print(num1)
print(num2)

num = 175e3
print(num)

# border to inf
print(2e308)
