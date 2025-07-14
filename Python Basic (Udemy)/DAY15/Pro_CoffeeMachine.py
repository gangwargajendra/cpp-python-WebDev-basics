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
    "money": 0,
}

def display_report() :
    symbol = ["ml", "ml", "g", "$"]
    i = 0
    for items in resources:
        if i != 3 :
            print(f"{items}: {resources[items]}{symbol[i]}")
        else :
            print(f"{items}: {symbol[i]}{resources[items]}")
        i += 1

def is_enough_resources(drink):
    drink_data = MENU[drink]
    ingredients_data = drink_data["ingredients"]
    for material in ingredients_data :
        if ingredients_data[material] > resources[material] :
            print(f"Sorry there is not enough {material}.")
            return False
    return True

def input_coins() :
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total_money = quarters * .25 + dimes * .1 + nickles * .05 + pennies * .01
    total_money = round(total_money , 2)
    return total_money

def is_enough_money_inserted(drink, money_inserted) :
    drink_data = MENU[drink]
    drink_cost = drink_data["cost"]
    if money_inserted >= drink_cost :
        exchange_money = round(money_inserted - drink_cost , 2)
        print(f"Here is ${exchange_money} in change.")
        return True
    return False

def make_changes_in_resources(drink) :
    drink_data = MENU[drink]
    drink_cost = drink_data["cost"]
    resources["money"] += drink_cost
    ingredients_data = drink_data["ingredients"]
    for material in ingredients_data :
        resources[material] -= ingredients_data[material]

is_continue = True

while is_continue :
    promt_action = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if promt_action == "report" :
        display_report()
    elif promt_action == "espresso" or promt_action == "latte" or promt_action == "cappuccino" :
        if is_enough_resources(promt_action)  :
            money_inserted = input_coins()
            if is_enough_money_inserted(drink=promt_action, money_inserted=money_inserted) :
                print(f"here is your {promt_action} 🍵 Enjoy!")
                make_changes_in_resources(promt_action)
            else :
                print("Sorry that's not enough money. Money refunded.")
    elif promt_action == "off" :
        is_continue = False
