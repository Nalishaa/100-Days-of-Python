MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def not_enough_items(ingredients):
    if resources["water"] < ingredients["water"]:
        return "Water"
    elif resources["milk"] < ingredients["milk"]:
        return "Milk"
    elif resources["coffee"] < ingredients["coffee"]:
        return "Coffee"
    else:
        return False


def remaining(ingredients, cost):
    resources["water"] -= ingredients["water"]
    resources["milk"] -= ingredients["milk"]
    resources["coffee"] -= ingredients["coffee"]
    resources["money"] += cost


def making_money(ingredients, request, cost):
    # TODO 5. Only do this if we have enough things
    print("Insert your coins.")
    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.10
    nickels = int(input("How many nickels? ")) * 0.05
    pennies = int(input("How many pennies? ")) * 0.01
    total = quarters + dimes + nickels + pennies

    if total < cost:
        # TODO 6. check if money is enough. if not enough
        return "Sorry that's not enough money. Money refunded."
    else:
        change = total - cost
        # TODO 8. Deduct the used ingredients first
        remaining(ingredients, cost)
        # TODO 7. Calculate change and add the money to Money
        return f"Here is your change: ${change:.2f}\nHere is your {request}. Enjoy! ☕"


def coffee_machine_working(request):
    # TODO 4. check if ingredients are enough and print what is not enough
    if request == "espresso" or request == "latte" or request == "cappuccino":
        ingredients = MENU[request]["ingredients"]
        cost = MENU[request]["cost"]
        state = not_enough_items(ingredients)
        if state == False:
            print(making_money(ingredients, request, cost))
        else:
            print(f"Sorry there is not enough {state}.")
            return

    elif request == "report":
        # TODO 3. the blanks need to be filled with the current quantity
        print(f"Water: {resources['water']} ml")    # it's better to use single and double quotes to prevent confusion
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} g")
        print(f"Money: $ {resources['money']}")
        return

    else:
        print("Invalid option. Please choose espresso/latte/cappuccino, report, or off.")
        return


def coffee_machine():
    process_should_continue = True
    while process_should_continue:
        # TODO 1. this needs to be printed after every step done
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice == "off":
            process_should_continue = False
            print("Turning off 🔴")
            #  TODO 2. this should completely end the process
        else:
            coffee_machine_working(choice)


coffee_machine()
