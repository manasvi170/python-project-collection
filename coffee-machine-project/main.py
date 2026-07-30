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
profit=0.0
resources = {
    "water":300,
    "milk": 200,
    "coffee":100,
    "cost" :0.0,
}
emoji="☕"
def report(resources_updating):
    if drink=="report":
        print(f'''
            Water: {resources_updating["water"]}ml
            Milk: {resources_updating["milk"]}ml
            Coffee: {resources_updating["coffee"]}g
            Cost:$ {profit}
            ''')
    else:
        return resources_updating

def money():
    print("Please insert coins")
    penny=float(input("How many pennies($0.01) ? "))*0.01
    nickle=float(input("How many nickles($0.05) ? "))*0.05
    dime=float(input("How many dimes($0.10) ? "))*0.10
    quarter= float(input("How many quarters($0.25) ? "))*0.25
    total=penny + nickle + dime + quarter
    return round(total,2)

def check_resources(all_resources,checking_resources):  #checking_resources contain ingredients of chosen drink
    if all_resources["water"]>=checking_resources["water"]:
        if all_resources["coffee"]>=checking_resources["coffee"]:
            if drink=="espresso":
                return True
            if all_resources["milk"]>=checking_resources["milk"]:
                return True
            else:
                return "milk"
        else:
            return "coffee"
    else:
        return "water"


should_continue = True
while should_continue:
    print("\nWelcome to our virtual Coffee Vending Machine!")
    drink=input("What would you like ? espresso/latte/cappuccino:").lower()
    if drink == "espresso" or drink == "latte" or drink == "cappuccino":
        """First check if we have sufficient resources"""
        resource = check_resources(resources, MENU[drink]["ingredients"])
        if resource==True:
            """Then ask them about money """
            total=money()
            if total>=MENU[drink]["cost"]:   #total is the TOTAL money added by the customer
                change=total-MENU[drink]["cost"]
                print(f"Your Balance: ${total}\n")
                print(f"\nHere is ${round(change,2)} dollars in change")
                print(f"Here is your {drink}{emoji}.Enjoy!\n")
                profit+=MENU[drink]["cost"]  #Profit added after customer purchased the drink
                resources['water']-=MENU[drink]["ingredients"]["water"]
                resources["coffee"]-=MENU[drink]["ingredients"]["coffee"]
                if drink!="espresso":
                    resources["milk"]-=MENU[drink]["ingredients"]["milk"]
            else:
                print(f"Your Balance: ${total}\n")
                print(f"Sorry that`s not enough money for {drink}!Your ${total} is refunded.\nThe {drink} is ${MENU[drink]["cost"]}\n")
        else:
            print(f"Sorry there is not enough {resource}")
            should_continue=False
    if drink=="off":
        should_continue=False
    if drink=="report":
        report(resources)





