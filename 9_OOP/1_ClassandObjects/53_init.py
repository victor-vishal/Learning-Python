# __init__ method is called a constructor
# it is always excuted when an object of a class is created

# even if we do not define a constructor in our class, python provides a default constructor for us

# objectname = ClassName()  # the parenthesis here are actually used for calling the constructor of the class

#eg
class Student:
    name = "Vishal"
    def __init__(self):#constructor always takes self as first argument
        print("Constructor is called")
        print(self)#<__main__.Student object at 0x00000138B6BA86E0>

s1 = Student()  # here the constructor is called automatically
#thus the print statement is executed
#SELF keyword
# the self keyword act as a place holder for the object that will be created.
# it points or refrences the object that is created from the class