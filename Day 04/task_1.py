import random
# random.randint a <= N <= b (whole number)
random_integer=random.randint(-10,10)
print(random_integer)

# random.random 0.0 <= X < 1.0 (float)
number_bet_0_and_1=random.random()
print(number_bet_0_and_1)

# scaling the range 0 <= X < 22 (float)
number_bet_0_and_1=random.random() * 22
print(number_bet_0_and_1)

# random.uniform a <= N <= b
# The end-point value b may or may not be included in the range depending on floating-point rounding
random_float=random.uniform(1,20)
print(random_float)

# Heads or Tails program
heads_or_tails=random.randint(0,1)
if heads_or_tails==0:
    print("Heads")
else:
    print("Tails")