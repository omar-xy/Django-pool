class HotBeverage:
    def __init__(self, name = "hot beverage", price = 0.3):
        self.name = name;
        self.price = price;
    def description(self):
        return "Just some hot water in a cup."
    def __str__(self):
        return f"name: {self.name}\nprice: {self.price:.2f}\ndescription: {self.description()}"

class Coffee(HotBeverage):
    def __init__(self):
        super().__init__(name = "Coffee", price = 0.7)
    def description(self):
        # OVERIDE THE ACTUAL FUNC
        return "A coffee, to stay awake."

class Tea(HotBeverage):
    def __init__(self):
        super().__init__(name = "Tea", price = 0.30)
    def description(self):
        return "Just some hot water in a cup."

class Chocolate(HotBeverage):
    def __init__(self):
        super().__init__(name = "Chocolate", price = 0.50)
    def description(self):
        return "Chocolate, sweet chocolate..."

class Cappuccino(HotBeverage):
    def __init__(self):
        super().__init__(name = "Cappuccino", price = 0.40)
    def description(self):
        return "Un po’ di Italia nella sua tazza!"

prod = Coffee()
print(prod)