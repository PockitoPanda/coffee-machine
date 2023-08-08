from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



def main():
    coffeemaker = CoffeeMaker()
    menu = Menu()
    moneymachine = MoneyMachine()
    
    while True:
        choice = input(f"What would you like? {menu.get_items()}report/off: ")
        if choice == "report":
            coffeemaker.report()
            moneymachine.report()
        elif choice == "off":
            break
        else:
            coffee = menu.find_drink(choice)
            if coffee is None:
                continue
            elif coffeemaker.is_resource_sufficient(coffee):
                if moneymachine.make_payment(coffee.cost):
                    coffeemaker.make_coffee(coffee)
    


    
        
    

    
    
main()