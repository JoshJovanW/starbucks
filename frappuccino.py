from coffee import Coffee

class Frappucino(Coffee):
    def details(self):
        return("It consists of coffee or crème base, blended with ice and other various ingredients, usually topped with whipped cream and flavored syrups")

    def add_topping(self, topping, price):
        if topping == "with extra jelly":
            print("sorry this drink cant use extra jelly, please use another topping.")
        else:
            self.topping = topping
            self.price += price
