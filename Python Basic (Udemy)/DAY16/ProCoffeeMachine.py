from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_continue = True

while is_continue :
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ").lower()
    if choice == "off" :
        is_continue = False
    elif choice == "report" :
        coffee_maker.report()
        money_machine.report()
    else :
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) :
            if money_machine.make_payment(drink.cost) :
                coffee_maker.make_coffee(drink)
