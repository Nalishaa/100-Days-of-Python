print("Welcome to the Tip Calculator!")
bill=float(input("What was the total bill? $"))
tip=int(input("How much tip would you like to give? 10, 12, or 15? "))
people=int(input("How many people to split the bill? "))
tip=bill*(tip/100)
bill+=tip
bill/=people
print(f"Each person should pay: ${bill:.2f}")