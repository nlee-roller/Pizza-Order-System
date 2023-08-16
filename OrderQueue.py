from Pizza import Pizza
from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza
from PizzaOrder import PizzaOrder

class OrderQueue:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i].time < self.heapList[i // 2].time:
                temp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = temp
            i = i // 2

    def minChild(self, i):
        if (i * 2 + 1) > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2].time < self.heapList[i*2+1].time:
                return i * 2
            else:
                return i * 2 + 1

    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i].time > self.heapList[mc].time:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def addOrder(self, pizzaOrder):
        self.insert(pizzaOrder)

    def processNextOrder(self):
        if self.currentSize < 1:
            raise QueueEmptyException
        else:
            return self.delMin().getOrderDescription()

    


class QueueEmptyException(Exception):
    pass
