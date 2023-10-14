menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

resources = {"water": 300, "milk": 200, "coffee": 100, "money": 0}

options = list(menu)

water_required = 0
milk_required = 0
coffee_required = 0

water_usage = [ ]
milk_usage =  [ ]
coffee_usage = [ ]

water_used = 0
milk_used = 0
coffee_used = 0

operation = 'on'
while operation == 'on':

    entry = (input("What would you like? (espresso/latte/cappuccino): \n")).lower()

    item_details = menu.get(entry)
    cost = item_details.get("cost")

    valid_entry = False
    while valid_entry == False:
        if entry in options or entry == 'report':
            valid_entry = True
            break
        else:
            print(f"Sorry, we do not have {entry} in our menu. Please chose an item from our menu")
        entry = (input("What would you like? (espresso/latte/cappuccino): \n")).lower()

    x = list(item_details.values())
    x = x[0]
    water_required = x.get('water')
    milk_required = x.get('milk')
    coffee_required = x.get('coffee')
    water_usage.append(water_required)
    water_used = sum(water_usage)
    milk_usage.append(milk_required)
    milk_used = sum(milk_usage)
    coffee_usage.append(coffee_required)
    coffee_used = sum(coffee_usage)
    if entry in options:
        print("Please insert coins.")
        quarters = float(input("how many quarters?: "))
        dimes = float(input("how many dimes?: "))
        nickles = float(input("how many nickles?: "))
        pennies = float(input("how many pennies?: "))
        money_entered = (pennies / 100 + nickles / 20 + dimes / 10 + quarters / 4)

        change = money_entered - cost
        change = round(change, 2)

        if money_entered > cost:
            print(f"Here is ${change} in change.")
            print(f"Here is your {entry}☕. Enjoy!")
        elif money_entered < cost:
            print(f"Sorry that's not enough money. Your ${money_entered} refunded.")
        else:
            print(f"Here is your {entry}☕. Enjoy!")

        item_details = {'ingredients': {'water': 200, 'milk': 150, 'coffee': 24}, 'cost': 2.5}
