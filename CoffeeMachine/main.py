import help


in_use_resources = help.resources
machine_amount = []
coins = {'quarters': 0.25, 'dimes': 0.10, 'nickles': 0.05, 'pennies': 0.01}


# TODO: 3 - Print report.
def print_report():
    for k, v in in_use_resources.items():
        k = k.title()
        if k == "Coffee":
            print(f"{k}: {v}g")
        else:
            print(f"{k}: {v}ml")
    print(f"Money: ${sum(machine_amount)}")


# TODO: 4 - Check resources sufficient?
def check_resources(drink):
    for i in help.MENU[drink]['ingredients']:
        drink_resource = help.MENU[drink]['ingredients'][i]
        if drink_resource <= in_use_resources[i]:
            return True
        else:
            print(f"Sorry there is not enough {i}")
            return False


# TODO: 5 - Process coins.
def process_coins(drink):
    user_amount = 0
    drink_cost = help.MENU[drink]['cost']
    print("Please insert coins.")
    for k, v in coins.items():
        num_coins = float(input(f"how many {k}? ${v}: "))
        user_amount = user_amount + (v * num_coins)
    if user_amount >= drink_cost:
        change = user_amount - drink_cost
        if change > 0:
            print(f"Here is ${round(change, 2)} in change.")
        machine_amount.append(drink_cost)
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


# TODO: 7 - Make Coffee.
def make_coffee(drink):
    print(f"Preparing your {drink}...")
    for i in help.MENU[drink]['ingredients']:
        drink_resource = help.MENU[drink]['ingredients'][i]
        if drink_resource <= in_use_resources[i]:
            in_use_resources[i] = in_use_resources[i] - drink_resource

    print(f"Here is your {drink} ☕️. Enjoy!")


# TODO: 1 - Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
def prompt_drink():
    coffee_type = input("What would you like? (espresso - $1.50 / latte - $2.50/ cappuccino - $3.00): ")
    return coffee_type


def error(user_option):
    print(f"We cannot produce your {user_option} now, please try again later")


def start():
    is_machine_on = True
    print(help.logo)
    while is_machine_on:
        user_option = prompt_drink()
        # TODO: 2 - Turn off the Coffee Machine by entering “off” to the prompt.
        if user_option == "espresso" or user_option == "latte" or user_option == "cappuccino":
            is_resource_enough = check_resources(user_option)
            # TODO: 6 - Check transaction successful?
            if is_resource_enough:
                is_coins_enough = process_coins(user_option)
                if is_coins_enough:
                    make_coffee(user_option)
            else:
                error(user_option)
        elif user_option == "report":
            print_report()
        elif user_option == "off":
            is_machine_on = False
            print("Shutting down coffee machine")
        else:
            print("Option invalid")


start()
