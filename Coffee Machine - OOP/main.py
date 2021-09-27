from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice in ['latte', 'cappuccino', 'espresso', 'off', 'report']:
        if choice == "off":
            print("BAAAAAAAAAAAAIIIIIII")
            is_on = False
        elif choice == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(choice)
            is_enough_ingredients = coffee_maker.is_resource_sufficient(drink)
            is_payment_successful = money_machine.make_payment(drink.cost)
            if is_enough_ingredients and is_payment_successful:
                coffee_maker.make_coffee(drink)
    else:
        print("Invalid Choice\n")
        continue
