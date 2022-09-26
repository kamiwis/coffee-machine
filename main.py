import os
from menu import MENU, resources
from helpers import prompt_user, print_report, check_resources, process_coins

def main():
    machine_off = False
    
    while not machine_off:
        # Prompt user - every time an action is completed.
        user_choice = prompt_user()

        # If user enters 'off' to prompt - code will end execution.
        if user_choice == "off":
            os.system("clear")
            machine_off = True
            return
    
        # If user enters 'report' to prompt - print a report of all resources and total money.
        if user_choice == "report":
            print_report(resources)

        #  If user enters a drink, check if resources are sufficient for that drink.
        if user_choice in ["espresso", "latte", "cappuccino"]:
            enough_resources = check_resources(user_choice, resources)
            # If there are enough resources, process coins.
            if enough_resources:
                print("Please insert coins.")
                total_coins = process_coins()
                # If users gives exact change, give drink
                if total_coins >= MENU[user_choice]["cost"]:
                    # Deduct ingredients from resources
                    resources["milk"] -= MENU[user_choice]["ingredients"]["milk"]
                    resources["water"] -= MENU[user_choice]["ingredients"]["water"]
                    resources["coffee"] -= MENU[user_choice]["ingredients"]["coffee"]
                    # Add cost of drink to resources
                    resources["money"] += MENU[user_choice]["cost"]
                    # Find difference between what user paid and the price of the drink.
                    difference = total_coins - MENU[user_choice]["cost"]
                    # If the user over-paid, return change.
                    if difference > 0:
                        print("Here is your ${:.2f} change.".format(difference))
                    print(f"Here is your {user_choice} ☕ Enjoy!")
                    continue
                # If the user did not give enough money, inform user.
                else:
                    print("Sorry that's not enough money. Money refunded.")
                    continue

if __name__ == "__main__":
    main()
