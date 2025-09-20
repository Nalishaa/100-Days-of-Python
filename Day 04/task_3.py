import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
# Method 1
bill=random.randint(0,4)
print(friends[bill]+" will pay the bill.")

# Method 2
print(random.choice(friends)+" will pay the bill.")