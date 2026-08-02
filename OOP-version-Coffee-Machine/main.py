from menu import Menu ,MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import art
menu_of_drink=Menu()
coffee_maker=CoffeeMaker()
money_machine=MoneyMachine()
machine_on=True

while machine_on:
    print("Welcome to my upgraded version of Coffee Maker🎛️🍵")
    print(art.machine)
    print(f"What would you like to have?🧸☕🍂˚ ༘ ೀ⋆｡˚\n({menu_of_drink.get_items()})")
    drink=input("Your Drink: ~")

    if drink=="latte"or drink=="espresso" or drink=="cappuccino":
        order = menu_of_drink.find_drink(drink)
        all_good=coffee_maker.is_resource_sufficient(order) # First checking the ingredient sufficiency!
        if all_good:
            all_payment=money_machine.make_payment(order.cost)
            print(all_payment)
            if all_payment:
                coffee_maker.make_coffee(order)
                print("🧸☕🍂˚ ༘ ೀ⋆｡˚")
                print(art.hot_coffee)
    if drink=="report":
        print("\n")
        print(f"{coffee_maker.report()}")
        print(f"{money_machine.report()}")
    if drink=="off":
        machine_on=False