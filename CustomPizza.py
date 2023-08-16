from Pizza import Pizza
class CustomPizza(Pizza):
    def __init__(self, size):
        super().__init__(size)
        if self.size == "S":
            self.setPrice(8.00)
        elif self.size == "M":
            self.setPrice(10.00)
        elif self.size == "L":
            self.setPrice(12.00)
        self.toppingList = []

    def addTopping(self, topping):
        self.toppingList.append(topping)
        if self.size == "S":
            self.price += .50
        elif self.size == "M":
            self.price += .75
        elif self.size == "L":
            self.price += 1.00

    def getPizzaDetails(self):
        toppings = ""
        for item in self.toppingList:
            toppings += "\t+ " + item + "\n"
        return f"CUSTOM PIZZA\nSize: {self.size}\nToppings:\n{toppings}Price: ${self.price:.2f}\n"
        
