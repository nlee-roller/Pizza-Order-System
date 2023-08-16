from Pizza import Pizza
from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza
class PizzaOrder:
    def __init__(self, time):
        self.pizzas = []
        self.time = time

    def getTime(self):
        return self.time

    def setTime(self, time):
        self.time = time

    def addPizza(self, pizza):
        self.pizzas.append(pizza)

    def getOrderDescription(self):
        orderString = "******\n"
        orderString += f"Order Time: {self.time}\n"
        price = 0
        for item in self.pizzas:
            orderString += item.getPizzaDetails() + "\n" + "----" + "\n"
            price += item.getPrice()
        orderString += f"TOTAL ORDER PRICE: ${price:.2f}\n"
        orderString += "******\n"
        return orderString

