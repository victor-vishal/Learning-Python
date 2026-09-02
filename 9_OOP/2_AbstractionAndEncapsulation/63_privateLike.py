# Unlike other languages like c++ or Java,
# python doesnt have access modifiers like public, private, protected etc.
# Python doesnt use any keyword to declare an attribute or method private
# It uses a naming convention to indicate that an attribute or method is private.

# name is public attribute
# _name is protected attribute
# __name is private attribute

class Bank:
    def __init__(self, name, accnum, password):
        self.name = name
        self.__accnum = accnum #the 2 underscores make it private
        self.__password = password

    def showpass(self):
        print(f"Hi {self.name}! your password is {self.__password}")

b1 = Bank("Vishal", 123456, "ABC")

#private methods or attributes cant be accessed outside the class. They can only be accessed inside the class.

#here we access the private attribute using a public method
#its called encapsulation. 

# print(b1.__accnum) # private attribute cant be accessed outside class

b1.showpass() # private attribute can be accessed inside class