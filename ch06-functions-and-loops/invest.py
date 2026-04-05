def invest(amount, rate, years):
    '''Display year on year growth of an initial investment'''
    for y in range(1, years + 1):
        amount = amount * (1 + rate)
        print(f"year {y}: ${amount:,.2f}")

x = float(input("Please enter an initial amount: "))
y = float(input("Please enter a rage: "))
z = int(input("Please enter a number of years: "))

invest(x, y, z)

