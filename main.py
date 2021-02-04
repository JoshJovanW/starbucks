from price import price_Menu

from soylatte import SoyLatte

from frappucino import Frappucino

from icecoffee import IceCoffee

from macchiato import Macchiato

from menu import Menu

from orders import Order


def main():
    Menu()
    price_Menu()

    exit = False
    Orders = Order()

    while exit == False:
        order = None

        drink = input("what do you want to order? Type SL for Soy Latte , JCF for Java chip Frappucino, ICJ for Ice Coffe Jelly and CM for Caramel macchiato.\n").lower()
   
        if drink == "sl":
            order = SoyLatte("soy latte", 4.25, "tall", "normal", "without topping")
    
        elif drink == "jcf":
            order = Frappucino("java chip frappucino", 3.45, "tall", "normal", "without topping")

        elif drink == "icj":
            order = IceCoffee("ice coffee jelly", 3.55, "tall", "normal", "without topping")

        elif drink == "cm":
            order = Macchiato("caramel macchiato", 4.99, "tall", "normal", "without topping")

        info = input("\nDo you want to know about the ingredients in your drink? Type (y/n)\n").lower()

        if info == "y":
            print(order.details())

        sugar = input("\ndo you want your drink to be less sugar or normal? type 'less'/'normal' \n").lower()

        if sugar == "less":
            order.less_sugar()

        size = input("\nwhat size do you want? Type T for Tall, G for Grande, V for Venti. \n").lower()

        if size == "t":
            order.change_size(0, "Tall")

        elif size == "g":
            order.change_size(0.7, "Grande")

        elif size == "v":
            order.change_size(1, "Venti")

        boolean = input("\ndo you want to add topping for your coffee? Type Yes or no. *some toppings are not available for specific drinks\n").lower()

        if boolean == "yes":
            topping_present = False
            while topping_present == False:
                topping = input("\nWhich topping do you want? Type AS to add extra 2 shots, WC for extra Whip Cream, J for extra Jelly and CF for extra Cloud Foam.\n").lower()
            
                if topping == "as":
                    order.add_topping("with 2 extra shots", 0.5)

                elif topping == "j":
                    order.add_topping("with extra jelly", 2)

                elif topping == "wc":
                    order.add_topping("with extra whip cream", 2)
            
                elif topping == "cf":
                    order.add_topping("with extra cloud foam", 1)

                if order.topping != "without topping":
                    topping_present = True

        Orders.add_order(order)
        another_drink = input("\ndo you want to order another drink?Type (y/n) to continue\n").lower()

        if another_drink == "n":
            exit = True

    else:
        total_price = Orders.verify_payment()
         
        print(f'Your total bill is ${total_price["payment"][0]}')
        if total_price["payment"][1] == "cash":
            dollars = int(input("How much Dollars do you want to give? \n"))
         

            print(f'Your change is ${(dollars - total_price["payment"][0])}')

        elif total_price["payment"][1] == "credit":
            print(f'${total_price["payment"][0]} have been deducted from you account.')

        print("thank you for ordering at starbucks")


main()

    


