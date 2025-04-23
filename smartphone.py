class smartphone:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.available = True

    def buy(self, quantity):
        if self.available and quantity <= self.quantity:
            self.quantity -= quantity
            if self.quantity == 0:
                self.available = False
            return f" {self.quantity} {self.name} bought successfully"
            return f"Not enough {self.name} in stock"
    
    def sell(self):
        if self.available:
            self.available = True
            return f" {self.quantity} {self.name} sold successfully"