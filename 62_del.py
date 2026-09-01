# del is used to delete a object property or an entire object. 

class Car:
    def __init__(self, company, model):
        self.company = company
        self.model = model

    def display(self):
        print(f"This is a car")

    def display2(self):
        print(f"This is a car using display2 method")
        
c1 = Car("Toyota", "Camry")
print(c1.company)
print(c1.model)
c1.display()
c1.display2()

# DELETING a method
# you cant delete a method from an object, since methods live in class

# del c1.display # ERROR: AttributeError: display

#How to actually delete a method

# 1. Delete the method from the class affects all instances
del Car.display #dont use () #del Car.display() gives error

# 2. Delete the method from the object only affects that instance
# we can achieve this by blocking the method only for that instance by assigning it to None

c1.display2 = None # Assigning None overrides the class lookup, masking the method for c1 while leaving other instances unaffected.

# This technique is called attribte masking or shadowing.
# # Python checks the instance dictionary BEFORE the class dictionary.
# # creating an instance variable with the same name shadows (masks) the class method.
# # So python finds none first and never reaches the class


# c1.display2() # ERROR: TypeError: 'NoneType' object is not callable

del c1 # deletes the whole object c1