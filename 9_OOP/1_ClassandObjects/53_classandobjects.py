class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def details(self):
        print(f"The Car is {self.color} {self.brand}")


car1 = Car("Red", "BMW")
car1.details()