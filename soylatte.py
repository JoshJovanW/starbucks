from coffee import Coffee

class SoyLatte(Coffee):
    def details(self):
        return("The layers of espresso and steamed milk are mixed together and topped with a light layer of foam. The drink is creamier and the coffee flavor is more subtle.")

    def add_topping(self, topping, price):
        if topping == "with extra cloud foam":
            print("sorry this drink cant use cloud foam, please choose another topping.")
        else:
            self.topping = topping
            self.price += price
