fruits = ["Cherry","Apple","Pear"]
# Accessing Items in Lists
print(fruits[0])

# Negative Indices
print(fruits[-1]) # gives the last item
print((fruits[-2]))

# Modifying Items
fruits[0]="Grapes"
print(fruits)

# Adding Items at the End
fruits.append("Pineapple")
print(fruits)

# Adding a list of Items
fruits.extend(["Mango","Watermelon"])
print(fruits)