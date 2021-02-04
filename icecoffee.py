from coffee import Coffee

class IceCoffee(Coffee):
    def details(self):
        return("Freshly brewed Starbucks® Iced Coffee Blend served chilled and sweetened over ice. An absolutely, seriously, refreshingly lift to any day")

    def add_topping(self, topping, price):
        if topping == "with extra whip cream":
            print("sorry this drink cant use whip cream, please choose another one topping.")
        else:
            self.topping = topping
            self.price += price
