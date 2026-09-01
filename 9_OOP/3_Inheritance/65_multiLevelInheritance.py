# in python inhertance has the following types:
# 1. Single Inheritance
# 2. Multiple Inheritance
# 3. Multilevel Inheritance

#Multilevel Inheritance: A child class is derived from a parent that is further derived from grandparent and so on.

class Grandparent:
    def __init__(self):
        print(f"This is grandparent class!")

    @staticmethod
    def walk():
        print("Person is walking")
    @staticmethod
    def eat():
        print("Person is eating")

class Parent(Grandparent):
    def __init__(self):
        print(f"This is parent class!")

    @staticmethod
    def talk():
        print("Person is talking")

class Child(Parent):
    def __init__(self):
        print(f"This is child class!")

    @staticmethod
    def play():
        print("Person is playing")

c1 = Child()
c1.walk() # inherited from grandparent class
c1.talk() # inherited from parent class
c1.play() # method of child class