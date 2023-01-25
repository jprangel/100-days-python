from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
my_money_machine = MoneyMachine()
my_coffee_maker = CoffeeMaker()
my_menu = Menu()

while is_on:
    options = my_menu.get_items()
    user_option = input(f"What would you like? {options}: ")
    if user_option == "off":
        is_on = False
    elif user_option == "report":
        my_coffee_maker.report()
        my_money_machine.report()
    else:
        drink = my_menu.find_drink(user_option)
        if drink is not None:
            is_resource_enough = my_coffee_maker.is_resource_sufficient(drink)
            if is_resource_enough:
                is_coins_enough = my_money_machine.make_payment(drink.cost)
                if is_coins_enough:
                    my_coffee_maker.make_coffee(drink)
