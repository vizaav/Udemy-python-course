from menu import MENU

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


class Drink:
    def __init__(self, name,  cost, **ingredients,):
        self.name = name
        self.ingredients = ingredients
        self.cost = cost


drinks = []
for drink in MENU:
    drinks.append(Drink(drink,  cost=float(MENU[drink]["cost"]), **MENU[drink]["ingredients"]))
    print(drink, MENU[drink]["ingredients"], float(MENU[drink]["cost"]))

coins = {"quarters": 0.25, "dimes": 0.10, "nickles": 0.05, "pennies": 0.01}


def check_resources(drink):
    for ingredient in drink.ingredients:
        if drink.ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    total = 0
    for coin in coins:
        print(f"How many {coin}?:")
        total += int(input()) * coins[coin]
    return total


looping = True
while looping:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "off":
        exit()
    elif choice == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g")
    elif choice == "espresso":
        if check_resources(drinks[0]):
            inserted_coins = process_coins()
            if inserted_coins == drinks[0].cost:
                print("Here is your espresso. Enjoy!")
                for ingredient in drinks[0].ingredients:
                    resources[ingredient] -= drinks[0].ingredients[ingredient]
            elif inserted_coins > drinks[0].cost:
                print(f"Here is your espresso and ${round(inserted_coins - drinks[0].cost, 2)} in change. Enjoy!")
                for ingredient in drinks[0].ingredients:
                    resources[ingredient] -= drinks[0].ingredients[ingredient]
            else:
                print("Sorry, that's not enough money. Money refunded.")
    elif choice == "latte":
        if check_resources(drinks[1]):
            inserted_coins = process_coins()
            if inserted_coins == drinks[1].cost:
                print("Here is your espresso. Enjoy!")
                for ingredient in drinks[1].ingredients:
                    resources[ingredient] -= drinks[1].ingredients[ingredient]
            elif inserted_coins > drinks[1].cost:
                print(f"Here is your espresso and ${round(inserted_coins - drinks[1].cost, 2)} in change. Enjoy!")
                for ingredient in drinks[1].ingredients:
                    resources[ingredient] -= drinks[1].ingredients[ingredient]
            else:
                print("Sorry, that's not enough money. Money refunded.")
    elif choice == "cappuccino":
        if check_resources(drinks[2]):
            inserted_coins = process_coins()
            if inserted_coins == drinks[2].cost:
                print("Here is your espresso. Enjoy!")
                for ingredient in drinks[2].ingredients:
                    resources[ingredient] -= drinks[2].ingredients[ingredient]
            elif inserted_coins > drinks[2].cost:
                print(f"Here is your espresso and ${round(inserted_coins - drinks[2].cost, 2)} in change. Enjoy!")
                for ingredient in drinks[2].ingredients:
                    resources[ingredient] -= drinks[2].ingredients[ingredient]
            else:
                print("Sorry, that's not enough money. Money refunded.")
