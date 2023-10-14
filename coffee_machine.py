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

options = ["espresso", "latte", "cappuccino"]

water_usage = [ ]
milk_usage =  [ ]
coffee_usage = [ ]
payment = [ ]
item_details = {}

operation = 'on'
while operation == 'on':

    entry = (input("What would you like? (espresso/latte/cappuccino): \n")).lower()

    valid_entry = False
    while valid_entry == False:
        if entry in options or entry == "report" or entry == "off":
            valid_entry = True
            break
        else:
            print(f"Sorry, we do not have {entry} in our menu. Please chose an item from our menu")
        entry = (input("What would you like? (espresso/latte/cappuccino): \n")).lower()

    if entry in options:
        item_details = menu.get(entry)
        cost = item_details.get("cost")

    if entry in options:

        x = list(item_details.values())
        x = x[0]
        water_required = x.get('water')
        milk_required = x.get('milk')
        coffee_required = x.get('coffee')
        water_usage.append(water_required)
        water_used = sum(water_usage)
        water_balance = resources.get("water") - water_used
        milk_usage.append(milk_required)
        milk_used = sum(milk_usage)
        milk_balance = resources.get("milk") - milk_used
        coffee_usage.append(coffee_required)
        coffee_used = sum(coffee_usage)
        coffee_balance = resources.get("coffee") - coffee_used
        payment.append(cost)
        money_balance = sum(payment)

        if water_balance < 0:
            print(f"Sorry! the available water is not sufficient to make a {entry}")
            break
        if milk_balance < 0:
            print(f"Sorry! the available water is not sufficient to make a {entry}")
            break
        if coffee_balance < 0:
            print(f"Sorry! the available water is not sufficient to make a {entry}")
            break

        if entry in options and entry != "report" and entry != "off":
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

        elif entry == "report":
            print(f"BALANCE REPORT\n----------------\nWater: {water_balance}ml \nMilk: {milk_balance}ml \nCoffee: {coffee_balance}g \nMoney: ${money_balance}")


        if entry == "off":
            operation != 'on'
            break










