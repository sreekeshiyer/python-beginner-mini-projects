import os

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
}


def brew_coffee(item_choice):
    """
    To make you some Yum Coffee :)
    """
    for resource in resources:
        resources[resource] -= MENU[item_choice]["ingredients"][resource]
    print(f"Here's your {item_choice} ☕ Enjoy!\n-----------\n")


def check_resources(item_choice):
    """
    To check if the machine has enough resources to brew your coffee.
    """
    for resource in resources:
        if resources[resource] < MENU[item_choice]["ingredients"][resource]:
            return {
                "result": False,
                "resource": resource
            }
    return {
        "result": True,
        "resource": "None",
    }


def report():
    print("Water: ", resources['water'])
    print("Milk: ", resources['milk'])
    print("Coffee: ", resources['coffee'])
    print("Money: $", machine_money)


call_turn_off = False
machine_money = 0

while not call_turn_off:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")

    valid_choices = ['espresso', 'latte', 'cappuccino', 'report', 'off', 'clear']
    if user_choice in valid_choices:
        if user_choice == 'clear':
            os.system("clear")
            continue
        elif user_choice == 'off':
            call_turn_off = True
            continue
        elif user_choice == 'report':
            report()
            print("\n-----------\n")
            continue
        
        resource_check = check_resources(user_choice)
        if resource_check["result"]:

            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            total_money_input = 0.01 * pennies + 0.05 * nickles + 0.1 * dimes + 0.25 * quarters

            if MENU[user_choice]["cost"] > total_money_input:
                print("Sorry, that's not enough money. Money Refunded")
            else:
                machine_money += total_money_input
                if total_money_input > MENU[user_choice]["cost"]:
                    change = total_money_input - MENU[user_choice]["cost"]
                    print("Here's ${:.2f} in change.".format(change))
                brew_coffee(user_choice)
                
        else:
            missing = resource_check["resource"]
            print(f"Sorry, there's not enough {missing}.")
            continue
    else:
        print("Invalid Input\n-----------\n")
        continue
