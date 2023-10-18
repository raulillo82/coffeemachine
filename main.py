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

machine_money = 0
run_machine = True

def get_drink():
    """Prompts user to enter a drink or one of the special options. Returns
    it"""
    drink_string = ""
    options = ["espresso", "latte", "cappuccino", "off", "report"]
    while drink_string not in options:
        drink_string = input("What would you like? (espresso/latte/cappuccino): ").lower()
        #import pdb; pdb.set_trace()
    return drink_string

def turn_off():
    """Turns off the machine and hence ends the program. No arguments"""
    print("Turning off the coffee machine for maintenance")
    return False

def print_report(resources):
    """Prints a report regarding resources and money. No arguments"""
    for resource in resources:
        print(resource + ": " + str(resources[resource]))
    print(f"Money: ${machine_money}")


def check_enough_resources(drink_string):
    """Returns a boolean stating whether the resources are enough for the given
    drink"""
    drink = MENU[drink_string]
    enough_resources = True
    for ingredient in drink["ingredients"]:
        if resources[ingredient] < drink["ingredients"][ingredient]:
            enough_resources = False
            print(f"Sorry, there is not enough {ingredient}")
    return enough_resources

def process_coins():
    """Queries user for the different kinds of coins and returns the total
    amount"""
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))
    return quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01

def check_enough_money(money, drink_string):
    """Returns a boolean stating whether the money was enough for the drink"""
    drink = MENU[drink_string]
    if money >= drink["cost"]:
        enough_money = True
        if money > drink["cost"]:
            change = "{:.2f}".format(money - drink["cost"])
            print(f"Here is ${change} in change")
    else:
        enough_money = False
        print("Sorry that's not enough money. Money refunded.")
    return enough_money

def make_coffee(drink_string):
    """Substracts required ingredients from resources and adds the money.
    Returns the cost"""
    drink = MENU[drink_string]
    for ingredient in drink["ingredients"]:
        resources[ingredient] -= drink["ingredients"][ingredient]
    print(f"Here is your {drink_string}")
    return drink["cost"]

while run_machine:
    drink_string = get_drink()
    if drink_string == "off":
        run_machine = turn_off()
    elif drink_string == "report":
        print_report(resources)
    else:
        if check_enough_resources(drink_string):
            if check_enough_money(process_coins(), drink_string):
                machine_money += make_coffee(drink_string)
