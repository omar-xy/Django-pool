
class HotBeverage:
    def __init__(self, name = "hot beverage", price = 0.3):
        self.name = name;
        self.price = price;
    def description(self):
        return "Just some hot water in a cup."
    def __str__(self):
        return f"name: {self.name}\nprice: {self.price:.2f}\ndescription: {self.description()}"

class Coffee: 

prod = HotBeverage()
print(prod)