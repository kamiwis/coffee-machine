import os
from menu import MENU, resources
from helpers import prompt_user, print_report, check_resources, process_coins

def main():

    # Prompt user - every time an action is completed.
    user_choice = prompt_user()

    # If user enters 'off' to prompt - code will end execution.
    if user_choice == "off":
        os.system("clear")
        return
    # If user enters 'report' to prompt - print a report of all resources and total money.
    if user_choice == "report":
        print_report(resources)

    #  If user enters a drink, check if resources are sufficient for that drink.
    if user_choice in ["espresso", "latte", "cappuccino"]:
        enough_resources = check_resources(user_choice, resources)
        if enough_resources:
            print("Please insert coins.")
            total_coins = process_coins()
            if total_coins == MENU[user_choice]["cost"]:
                print(f"Here is your {user_choice} ☕ Enjoy!")

# TODO Process coins if resources are sufficient.

# TODO If user doesn't input enough money, refund money.

# TODO If user inputs enough money, cost of drink gets added to machine as profit.

# TODO If user inputs too much money, machine offers change.


main()
