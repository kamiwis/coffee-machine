from menu import MENU, resources

def prompt_user():
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    return choice

def print_report(resources):
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: ${resources['money']}")

def check_resources(drink, resources):
    enough = True
    # Check water
    if MENU[drink]["ingredients"]["milk"] > resources["milk"]:
        print("Sorry there is not enough milk.")
        enough = False
    # Check milk
    if MENU[drink]["ingredients"]["water"] > resources["water"]:
        print("Sorry there is not enough water.")
        enough = False
    #Check coffee
    if MENU[drink]["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry there is not enough coffee.")
        enough = False
    return enough
    