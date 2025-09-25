# Functions with Outputs
def my_function():
    return 2*3

output=my_function()
print(output)


# Formatting names without using title function
def format_name():
    name=""
    first_1=""
    first_2=""
    f_name=input("Enter your first name.\n")
    l_name=input("Enter your last name.\n")
    for i in range(len(f_name)):
        if i == 0:
            first_1 = f_name[0].upper()
        else:
            first_1 += f_name[i].lower()

    for i in range(len(l_name)):
        if i == 0:
            first_2 = l_name[0].upper()
        else:
            first_2 += l_name[i].lower()

    name = first_1 +" "+ first_2
    return name
print(format_name())


# Formatting names using title function
first_name=input("Enter your first name.\n")
last_name=input("Enter your last name.\n")

def format_name(f_name,l_name):
    name = f_name + " " + l_name
    final_name = name.title()
    return final_name

print(format_name(first_name,last_name))


# Using one function's output as another function's input
def function_1(text):
    return text + " " + text

def function_2(text):
    return text.title()

output=function_2(function_1("hello"))
print(output)