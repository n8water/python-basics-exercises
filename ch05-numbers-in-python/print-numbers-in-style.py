n = 7.125
print(n)
print(f"The value of n is {n}")
print(f"The value of n is {n:.2f}")

n = 7.126
print(n)
print(f"The value of n is {n}")
print(f"The value of n is {n:.2f}")

print(n)
print(f"The value of n is {n}")
print(f"The value of n is {n:.1f}")

# add commas to numbers to make them more readable to users
# points or space does not work

n = 123456789
print(f"The value of n is {n:,}")

# rount and format number
n = 1234.56
print(f"The value of n is {n:,.2f}")

# ,.2f is useful for displaying currency values
balance = 2000.0
spent = 256.35
remaining = balance - spent
print(f"After spending ${spent:,.2f}, I was left with ${remaining:,.2f}")

# Percent % option
ratio = 0.9
print(f"Over {ratio:.1%} of Pythonistas say 'Real Python rocks!'")

# Display percentage with 2 decimal places
print(f"Over {ratio:.2%} of Pythonistas say 'Real Python rocks!'")

'''
1. Print the result of the calculation 3 ** .125 as a fixed-point number
with three decimal places.
'''
result = 3 ** .125
print(f"The result is {result:.3f}")

'''
2. Print the number 150000 as currency with the thousands grouped
with commas. Currency should be displayed with two decimal
places.
'''
currency = 150000
print(f"{currency:,.2f}")

'''
3. Print the result of 2 / 10 as a percentage with no decimal places.
The output should look like 20%.
'''
percentage = 2 / 10
print(f"{percentage:.0%}")
