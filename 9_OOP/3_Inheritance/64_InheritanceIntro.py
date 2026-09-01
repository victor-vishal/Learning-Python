# Inhertance is a concept in oops, where a child class can aquire(inherit) the properties and methods of a parent class.

class Car:
    color = "White"
    @staticmethod
    def start():
        print("Car started.")

    @staticmethod
    def stop():
        print("Car stopped.")

class Suzuki(Car): #we write parent name in parentheisis
    def __init__(self, model):
        self.model = model

    def display(self):
        print(f"Car model is {self.model} and color is {self.color}")
c1 = Suzuki("Swift")
c1.start() # inherited method from parent class
c1.color = "Red" # inherited attribute from parent class
c1.display() # method of child class