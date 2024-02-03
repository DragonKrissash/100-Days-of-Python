from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu=Menu()
moneymachine=MoneyMachine()
machine=CoffeeMaker()
turn_on=True
while turn_on:
    machine.report()
    print('What do you want from the following list: \n', menu.get_items())
    order = input()
    order = menu.find_drink(order)
    if order:
        if machine.is_resource_sufficient(order):
            if moneymachine.make_payment(order.cost):
                machine.make_coffee(order)
            else:
                turn_on=False
        else:
            turn_on=False
    else:
        turn_on=False

print(moneymachine.report())
