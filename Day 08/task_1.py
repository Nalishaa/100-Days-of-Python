# Basic Function
def greet():
    print("Hello")
    print("Hi")
    print("Hey")

greet()

# Functions with inputs
def greet_with_inputs(name):
    print(f"Hello {name}")
    print("How are you?")

Name=input("What is your name? ")
greet_with_inputs(Name)
greet_with_inputs("Jennie")

# Life in weeks (How many weeks are left?)
def life_in_weeks(age):
    total_weeks = 90 * 52
    time = total_weeks - age * 52
    print(f"You have {time} weeks left.")

life_in_weeks(20)