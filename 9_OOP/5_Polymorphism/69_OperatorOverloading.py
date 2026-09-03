#Operator Overloading is a type of polymorphism

print(2+3) # here + adds two numbers
print("Hello" + "World") # here + concatenates two strings
print([1,2] + [3,4]) # here + concatenates/merges two lists

print(type("Hello" + "World")) # <class 'str'>

# class str it is already  defined  + means concatenation of two strings. 
# similarly for int and list

# Dunder methods are the methods which have double underscores at the beginning and end of their names.
# AKA Mgic methods or special methods. These methods are used to implement operator overloading in Python.
# For example, the __add__ method is used for the + operator.

print(dir(int)) # prints attributes and methods of int class including dunder or magic methods like __add__, __sub__, __mul__ etc.