# # Target is the number up to which we count
# def fizz_buzz(target):
#     for number in range(1, target + 1):
#         if number % 3 == 0 or number % 5 == 0:
#             print("FizzBuzz")
#         if number % 3 == 0:
#             print("Fizz")
#         if number % 5 == 0:
#             print("Buzz")
#         else:
#             print([number])

# Target is the number up to which we count
def fizz_buzz(target):
    for number in range(1, target + 1):
        # use and (not or)
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        # use elif (not if)
        elif number % 3 == 0:
            print("Fizz")
        # use elif (not if)
        elif number % 5 == 0:
            print("Buzz")
        else:
            # remove square brackets []
            print(number)

fizz_buzz(10)