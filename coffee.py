class Coffee:
    def __init__(self, name, price, size, sugar, topping):
        self.name = name
        self.price = price
        self.size = size
        self.sugar = sugar
        self.topping = topping

    def __str__(self):
        return f"You ordered the {self.name} with {self.sugar} sugar, {self.topping}, size {self.size} drink. It costs ${self.price}"

    def less_sugar(self, sugar="less"):
        self.sugar = sugar

    def change_size(self, price, size):
        self.price += price
        self.size = size

    def add_topping(self, topping, price):
        self.topping = topping
        self.price += price
