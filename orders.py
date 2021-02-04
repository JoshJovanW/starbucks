class Order:
    def __init__(self):
        self.orders = []
        self.receipt = {}

    def add_order(self, order):
        self.orders.append(order)

    def verify_payment(self):
        total_price = 0 
        for idx, value in enumerate(self.orders):
            total_price += self.orders[idx].price

        payment_method = input("\nwhat do you want to pay with? Type 'cash' or 'credit' *if you use credit card you will get a 20 percent discount\n").lower()

        if payment_method == "credit":
            total_price = total_price - (total_price * 0.2)
            self.receipt["payment"] = [total_price, "credit"]

        elif payment_method == "cash":
            self.receipt["payment"] = [total_price, "cash"]

        return self.receipt
