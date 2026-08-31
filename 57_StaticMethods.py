#Methods in python are of the following types:
#1. Instance Methods
#2. Class Methods
#3. Static Methods

#1 Instace Methods are what we have been using so far. They take self as the first argument,
# using self is must even if we are not using it in the method. 

#To prevent the use of self in a method we can use class methods and static methods.

#Static Methods work at class level and doesnt require self parameter. 

#Synatx: 
# just write @staticmethod before the method definition.


class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod #decorator
    def result(marks): # this function doesnt use any class or object variable, and the marks parameter is passed manually, so we can make it static method 
        if marks >= 40:
            print("Pass")
        else:
            print("Fail")
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")