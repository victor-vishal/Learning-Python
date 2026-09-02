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