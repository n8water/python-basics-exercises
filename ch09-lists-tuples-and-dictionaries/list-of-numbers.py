# List of numbers

nums = [1, 2, 3, 4, 5]
print("nums = [1, 2, 3, 4, 5]")

total = 0
for number in nums:
    total += number

print(total)

# a much more succinct was of doing this in Python:
print("sum([1, 2, 3, 4, 5])")
print(sum([1, 2, 3, 4, 5]))
print("sum(nums)")
print(sum(nums))

# two other useful built-in functions for working with numers are
# min() and max()
print("min(nums):")
print(min(nums))
print("max(nums):")
print(max(nums))

# sum(), min(), and max() also work with tuples:
nums = (1, 2, 3, 4, 5)
print("sum((1, 2, 3, 4, 5))")
print(sum((1, 2, 3, 4, 5)))
print(min(nums))
print("max(nums):")
print(max(nums))
