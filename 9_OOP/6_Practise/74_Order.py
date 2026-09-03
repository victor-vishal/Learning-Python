# Create a class order which stores item and its price 
# use dunder function __gt__() to comvey that
# order 1> order 2 if price of order 1 is greater than price of order 2

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    # def compare (self, item2):
    #     if self.price >= item2.price:
    #         print(f"{self.item}  is expensive than {item2.item}")

    #     else:
    #         print(f"{self.item} is cheaper than {item2.item}")

    #MY ANSWER
    # def __gt__ (self, item2): 
    #         if self.price >= item2.price:
    #             #print(f"{self.item}  is expensive than {item2.item}")
    #             return True
    #         else:
    #             return False
    
    #SOLUTION
    def __gt__(self, item2):
        return self.price > item2.price

o1 = Order("Ghee", 1000)
o2 = Order("Paneer", 150)
# o1.compare(o2)
#o1>o
print(o2>o1) #returns False as price of o2 is not greater than price of o2
print(o1>o2) #returns True as price of o1 is greater than price of o2