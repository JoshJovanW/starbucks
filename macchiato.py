from coffee import Coffee

class Macchiato(Coffee):
    def details(self):
        return("Made with vanilla syrup, steamed milk, espresso and caramel sauce. The espresso in poured on top of the milk leaving a dark mark on top of the milk foam")
 
    def add_topping(self, topping, price):
        if topping == "with extra jelly":
            print("sorry this drink cant use extra jelly. please choose another topping.")
        else:
            self.topping = topping
            self.price += price
