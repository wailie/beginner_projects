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


profit = 0


def report():
    """report how much resources the machine has"""
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}ml\nMoney: ${profit}")


def espresso():
    """
    #1# get the resources and make the coffee(espresso). if the resource is used then it is subtracted from resources
    #2# the resource must be available in resources variable. (e.g. not less than ingredients)
    #3# if process_coin() is not 0 (which means not enough money) then update the new resources and make coffee
    """
    global resources, profit
    water_left = resources['water'] - MENU['espresso']['ingredients']['water']
    coffee_left = resources['coffee'] - MENU['espresso']['ingredients']['coffee']
    profit += MENU['espresso']['cost']
    if water_left >= 0 and coffee_left >= 0:
        if process_coin(MENU['espresso']['cost']) != 0:
            resources.update(water = water_left, coffee = coffee_left)
            return "Here is your espresso ☕. Enjoy!"
    else:
        if water_left < 0:
            return "Sorry not enough water."
        else:
            return "Sorry not enough coffee."


def latte():
    """
    #1# get the resources and make the coffee(latte). if the resource is used then it is subtracted from resources
    #2# the resource must be available in resources variable. (e.g. not less than ingredients)
    #3# if process_coin() is not 0 (which means not enough money) then update the new resources and make coffee
    """
    global resources, profit
    water_left = resources['water'] - MENU['latte']['ingredients']['water']
    milk_left = resources['milk'] - MENU['latte']['ingredients']['milk']
    coffee_left = resources['coffee'] - MENU['latte']['ingredients']['coffee']
    profit += MENU['latte']['cost']
    if water_left >= 0 and milk_left >= 0 and coffee_left >= 0:
        if process_coin(MENU['latte']['cost']) != 0:
            resources.update(water = water_left, milk = milk_left, coffee = coffee_left)
            return "Here is your latte ☕. Enjoy!"
    else:
        if water_left < 0:
            return "Sorry, not enough water."
        elif milk_left < 0:
            return "Sorry, not enough milk."
        else:
            return "Sorry, not enough coffee."


def cappuccino():
    """
    #1# get the resources and make the coffee(cappuccino). if the resource is used then it is subtracted from resources
    #2# the resource must be available in resources variable. (e.g. not less than ingredients)
    #3# if process_coin() is not 0 (which means not enough money) then update the new resources and make coffee
    """
    global resources, profit
    water_left = resources['water'] - MENU['cappuccino']['ingredients']['water']
    milk_left = resources['milk'] - MENU['cappuccino']['ingredients']['milk']
    coffee_left = resources['coffee'] - MENU['cappuccino']['ingredients']['coffee']
    profit += MENU['cappuccino']['cost']
    if water_left >= 0 and milk_left >= 0 and coffee_left >= 0:
        if process_coin(MENU['cappuccino']['cost']) != 0:
            resources.update(water = water_left, milk = milk_left, coffee = coffee_left)
            return "Here is your cappuccino ☕. Enjoy!"
    else:
        if water_left < 0:
            return "Sorry not enough water."
        elif milk_left < 0:
            return "Sorry not enough milk."
        else:
            return "Sorry not enough coffee."


def off():
    """when off is typed, the machine must stop"""
    global should_end
    should_end = True
    return 0


def process_coin(price):
    """
    #1# it asks coin amount and add it to total
    #2# if total less than price, refund
    #3# if total greater than price, give changes
    """
    # quarter = 0.25
    # dimes = 0.10
    # nickles = 0.05
    # pennies = 0.01
    print("Please insert coins.")
    quarters = float(input("how many quarters?: "))
    dimes = float(input("how many dimes?: "))
    nickles = float(input("how many nickles?: "))
    pennies = float(input("how many pennies?: "))
    quarters_amount = quarters * 0.25
    dimes_amount = dimes * 0.10
    nickles_amount = nickles * 0.05
    pennies_amount = pennies * 0.01
    total = quarters_amount + dimes_amount + nickles_amount + pennies_amount
    if total > price:
        change = total - price
        print(f"Your payment is successful. Here's ${round(change, 2)} in change.")
    elif total == price:
        print("Your payment is successful.")
    else:
        print("Sorry, you didn't insert enough coins. Refunded.")
        return 0


def refill():
    """
    when there is not enough resources, it will refill the resources to original amount
    """
    global resources
    resources.update(water = 300, milk = 200, coffee = 100)
    print("Resources refilled.")


command = {
    'report': report,
    'espresso': espresso,
    'latte': latte,
    'cappuccino': cappuccino,
    'off': off,
    'refill': refill,
    'profit': profit
}


should_end = False
while not should_end:
    prompt = input("What would you like? (espresso - $1.5/latte - $2.5/cappuccino - $3.0): ").lower()
    if prompt == "off" or prompt == "report" or prompt == "refill":
        command[prompt]()
    else:
        result = command[prompt]()
        if result != 0:
            print(result)

