def drink_available():
    """Checks if drink is available"""
    for i in MENU[preference]['ingredients']:
        if coffee_machine[i] < MENU[preference]['ingredients'][i]:
            print(f"We've run out of {i}")
            return False
        else:
            return True
def money_enough():
    """Checks if money paid by user is enough"""
    if total_paid >= MENU[preference]["cost"]:
        change = round(total_paid - MENU[preference]['cost'], 2)
        print(f"Your change is ${change}! Enjoy your {preference}")
        global profit
        profit = profit + MENU[preference]["cost"]
        return True
    else:
        print("Money's not enough")

        
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

coffee_machine = {"water": 300, "milk": 200, "coffee": 100}
profit = 0

is_on = True
while is_on == True:
    preference = input("What would you like? ")

    if preference == "report":
        print(f"Water: {coffee_machine['water']}ml")
        print(f"Milk: {coffee_machine['milk']}ml")
        print(f"Coffee: {coffee_machine['coffee']}g")
        print(f"Money: {profit}")
    elif preference == "off":
        is_on = False
    elif preference == "espresso" or "latte" or "cappuccino":
        #Check if drink is available
        if drink_available() == True:
            #If drink is available, get user to input money
            quarters = 0.25 * int(input("How many quarters? "))
            dimes = 0.10 * int(input("How many dimes? "))
            nickels = 0.05 * int(input("How many nickels? "))
            pennies = 0.01 * int(input("How many pennies? "))
            total_paid = quarters + dimes + nickels + pennies
            
            #Check is money is enough
            if money_enough() == True:
                #Make coffee
                for j in MENU[preference]["ingredients"]:
                    coffee_machine[j] = coffee_machine[j] - MENU[preference]["ingredients"][j]                
