# Methods are functions defined inside a class. 
# They are accessed using the dot operator on an instance of the class.
# Syntax: Object.method_name()

class Student:

    def __init__(self, name, age, roll_no):
        print("Constructor is called... ")
        self.name = name
        self.age = age
        self.roll_no = roll_no
        print(f"Student {self.name} is created\n")

    def display(self):
        print(f"Name: {self.name} Age: {self.age} Roll no. : {self.roll_no}\n")

s1 = Student("Vishal", 20, 65)
s2 = Student("Viktor", 20, 56)

s1.display()
var= s2.display()