from menu import MENU, resources

def prompt_user():
    """Prompts user for input and returns user's choice"""
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    return choice

def print_report(resources):
    """Takes resources dictionary as parameter and prints a report detailing the amount of resources
    left in the coffee machine."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: ${resources['money']}")

def check_resources(drink, resources):
    """Takes user's drink choice and resources dictionary as input.
    Checks to see if there are enough resoures in the machine to make the user's drink choice.
    If even one resources is lower than what the user needs to make their drink, returns False."""
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

def process_coins():
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
    return total
    