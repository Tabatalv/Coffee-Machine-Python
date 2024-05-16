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


def pricing(type_of_coffee):
    quarter = 0.25
    nickel = 0.05
    penny = 0.01
    dime = 0.10
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickels = float(input("How many dimes: "))
    pennies = float(input("How many pennies?: "))

    total_quarters = quarter * quarters
    total_dimes = dime * dimes
    total_nickels = nickel * nickels
    total_pennies = penny * pennies
    total_sum = round(total_pennies + total_dimes + total_nickels + total_quarters, 2)

    if MENU[type_of_coffee]["cost"] < total_sum:
        if MENU[type_of_coffee] == MENU["latte"] or MENU[type_of_coffee] == MENU["cappuccino"]:
            change = round(total_sum - MENU[type_of_coffee]["cost"], 2)
            resources["water"] = resources["water"] - MENU[type_of_coffee]["ingredients"]["water"]
            resources["milk"] = resources["milk"] - MENU[type_of_coffee]["ingredients"]["milk"]
            resources["coffee"] = resources["coffee"] - MENU[type_of_coffee]["ingredients"]["coffee"]
            print(f"Here is {change} in change.")
            print(f"Here is your {type_of_coffee} ☕. Enjoy!")
        else:
            change = round(total_sum - MENU[type_of_coffee]["cost"], 2)
            resources["water"] = resources["water"] - MENU[type_of_coffee]["ingredients"]["water"]
            resources["coffee"] = resources["coffee"] - MENU[type_of_coffee]["ingredients"]["coffee"]
            print(f"Here is {change} in change.")
            print(f"Here is your {type_of_coffee} ☕. Enjoy!")

    elif MENU[type_of_coffee]["cost"] > total_sum:
        print("Sorry, that's not enough money. Money refunded")
    elif MENU[type_of_coffee]["cost"] == total_sum:
        if MENU[type_of_coffee] == MENU["latte"] or MENU[type_of_coffee] == MENU["cappuccino"]:
            print(f"Here is your {type_of_coffee} ☕. Enjoy!")
            resources["water"] = resources["water"] - MENU[type_of_coffee]["ingredients"]["water"]
            resources["milk"] = resources["milk"] - MENU[type_of_coffee]["ingredients"]["milk"]
            resources["coffee"] = resources["coffee"] - MENU[type_of_coffee]["ingredients"]["coffee"]
        else:
            change = round(total_sum - MENU[type_of_coffee]["cost"], 2)
            resources["water"] = resources["water"] - MENU[type_of_coffee]["ingredients"]["water"]
            resources["coffee"] = resources["coffee"] - MENU[type_of_coffee]["ingredients"]["coffee"]
            print(f"Here is {change} in change.")
            print(f"Here is your {type_of_coffee} ☕. Enjoy!")
            print(resources["water"])


def resource_alert(type_of_coffee):
    if resources["water"] <= 0 and resources["milk"] <= 0 and resources["coffee"] <= 0:
        print("Sorry, we've run out of resources. See you next time!")
        play = False
    elif resources["water"] < MENU[type_of_coffee]["ingredients"]["water"] :
        print("Sorry, there's not enough water.")
        begin()


def begin():
    play = True
    while play:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice == "report":
            print(resources)
        else:
            resource_alert(choice)
            pricing(choice)


begin()
