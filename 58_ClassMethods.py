# class methods belongs to class itself
# it takes cls as the first parameter instead of self.
# Syntax:
# write @classmethod before the method definition.

# use differnce of class and static methods is that class methods can access class variables and methods, while static methods cannot.

# Use a class method when the function needs to talk to the class (to change a common variable like college_name or build a new student).

# Use a static method when the function is completely isolated and just does a random calculation or check, but you put it inside the class because it's related to students.

#### Here is the ultimate rule of thumb: If the method doesn't use a single variable from your class or instance, it should be static.
class Student:

    college_name = "ABC College"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod #decorator
    #this method acceses the class variable college_name and can change it
    def college(cls, new_college_name): 
        cls.college_name = new_college_name

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

    @staticmethod
    def result(marks): # this function doesnt use any class or object variable, and the marks parameter is passed manually, so we can make it static method 
        if marks >= 40:
            print("Pass")
        else:
            print("Fail")