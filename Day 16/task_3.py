from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_item = Menu()
coffee_maker_code = CoffeeMaker()
money_machine_code = MoneyMachine()

machine_on = True
while machine_on:
    order_name = input(f"What would you like? ({menu_item.get_items()}): ")

    if order_name == "off":
        print("Turning off 🔴")
        machine_on = False
    elif order_name == "report":
        coffee_maker_code.report()
        money_machine_code.report()
    elif order_name == "latte" or order_name == "espresso" or order_name == "cappuccino":
        inventory = menu_item.find_drink(order_name)
        available = coffee_maker_code.is_resource_sufficient(inventory)
        if available:
            payment_success = money_machine_code.make_payment(inventory.cost)
            if payment_success:
                coffee_maker_code.make_coffee(inventory)


