# Functions with more than one input
def greet_with(name,location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?\n")

# Position arguments
greet_with("Nalisha","Europe")

# Keyword arguments
greet_with(location="Korea",name="Nalisha")