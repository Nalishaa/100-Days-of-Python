# Format of making dictionaries
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}   # we end the last entry with a comma (optional) to make it easy to add items


# Retrieving things from a dictionary
print(programming_dictionary["Bug"])


# Adding things to a dictionary (can also be used to edit an existing entry)
programming_dictionary["Loop"]="The action of doing something over and over again."
programming_dictionary["Bug"]="Errors in a program."
print(programming_dictionary)


# Empty dictionary (can also be used to wipe out an existing dictionary)
dictionary = {}


# Loop through a dictionary
for key in programming_dictionary:
    print(key) # it will only print the keys not the values
    print(programming_dictionary[key])