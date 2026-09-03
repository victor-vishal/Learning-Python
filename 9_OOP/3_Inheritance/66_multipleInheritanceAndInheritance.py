# Multiple inhertiance: A child class is derived from more than one parent class.

class Mother:
    def __init__(self, name):
        self.name = name
        print(f"This is mother class!")

    def cook(self):
        print(f"{self.name} is cooking")

class Father:
    def __init__(self, name):
        self.name = name
        print(f"This is father class!")

    def drive(self):
        print(f"{self.name} is driving")

class Child(Mother, Father):
    def __init__(self, name):
        self.name = name
        print(f"This is child class!")
    
    def play(self):
        print(f"{self.name} is playing")

c1 = Child("Vishal")
c1.cook() # inherited from mother class
c1.drive() # inherited from father class
c1.play() # method of child class

#Super() is used to access methods of parent class in child class. 

#it allows for modifying or extending the functionality of inherited methods without completely overriding them.
print("===================")

class Car:
    def __init__(self, model, type):
        self.model = model
        self.type = type

    def start(self):
        print(f"{self.model} car started")

class Suzuki(Car):
    def __init__(self,color,model, type):
        self.color = color
        super().__init__(model, type) # calling parent class constructor using super()

    def display(self):
        print(f"Model: {self.model} \nType: {self.type} \nColor: {self.color}")

c1 = Suzuki("Red", "Swift", "Hatchback")
c1.display()

#we use super() to call the constructor of parent class
#and intialize the attributes of parent class in child class.
# that is we have attributs of parent class populated/initialized, withou creating a parent class object.