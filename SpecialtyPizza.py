from Pizza import Pizza
class SpecialtyPizza(Pizza):
    def __init__(self, size, name):
        super().__init__(size)
        if self.size == "S":
            self.setPrice(12.00)
        elif self.size == "M":
            self.setPrice(14.00)
        elif self.size == "L":
            self.setPrice(16.00)
        self.name = name

    def getPizzaDetails(self):
        return f"SPECIALTY PIZZA\nSize: {self.size}\nName: {self.name}\nPrice: ${self.price:.2f}\n"
        
