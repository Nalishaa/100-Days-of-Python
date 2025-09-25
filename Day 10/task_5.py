import art
print(art.logo)

# TODO: Write out the other 3 functions - subtract, multiply and divide.
def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

# TODO: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"
operations={
    "+":add, "-":subtract, "*":multiply, "/":divide, #we are storing functions not triggering them
}

# TODO: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary.
# 4 * 8 using the dictionary
# print(operations["*"](4,8))

# This is my approach
new_calc=True
while new_calc:
    first_num=float(input("What's the first number?: "))
    old_calc=True
    while old_calc:
        for key in operations:
            print(key )
        choice=input("Pick an operation: ")
        second_num=float(input("What's the next number?: "))
        output = operations[choice](first_num,second_num)
        print(f"{first_num} {choice} {second_num} = {output}")

        more=input(f"Type 'y' to continue calculating with {output}, or type 'n' to start new calculation: ").lower()
        if more == 'y':
            first_num=output
            new_calc=False
        else:
            print("\n"*20)
            old_calc=False



# Solution provided by the course
def calculation():
    first_num=float(input("What's the first number?: "))
    old_calc=True
    while old_calc:
        for key in operations:
            print(key )
        choice=input("Pick an operation: ")
        second_num=float(input("What's the next number?: "))
        output = operations[choice](first_num,second_num)
        print(f"{first_num} {choice} {second_num} = {output}")

        more=input(f"Type 'y' to continue calculating with {output}, or type 'n' to start new calculation: ").lower()
        if more == 'y':
            first_num=output
            new_calc=False
        else:
            print("\n"*20)
            old_calc=False
            calculation()

calculation()