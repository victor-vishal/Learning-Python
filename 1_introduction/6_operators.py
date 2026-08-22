#Arithmetic OPerators
print(2 + 3) #Addition
print(5 - 2) #Subtraction
print(4 * 3) #Multiplication
print(10 / 2) #Division
print(10 // 3) #Floor Division (returns the largest integer less than or equal to the result)
print(2 ** 3) #Exponentiation (2 raised to the power of 3
print(10 % 3) #Modulus (returns the remainder of the division)

#comparison operators it gives the output in boolean value (True or False)
x = 10
y = 5
print(x > y) #Greater than                      prints True
print(x < y) #Less than                         prints False
print(x == y) #Equal to                         prints False
print(x != y) #Not equal to                     prints True
print(x >= y) #Greater than or equal to         prints True
print(x <= y) #Less than or equal to            prints False

#logical operators
age =20
is_student = True
print(age>18 and is_student) #Logical AND (returns True if both conditions are true) prints True
print(age>18 or is_student) #Logical OR (returns True if at least one condition is true) prints True
print(not is_student) #Logical NOT (returns True if the condition is false) prints False
#unlike c++ in python we dont use if or else for logical operators we can directly use them in print statements or in any other expressions without the need for if or else statements.

#assignment operators
#the assignment operators include +=, -=, *=, /=, //=, **= and %= which are used to perform the operation and assign the result to the variable in a single step.
x = 10
x += 5 # x = x + 5
print(x) # prints 15
x -= 3 # x = x - 3
print(x) # prints 12
x *= 2 # x = x * 2
print(x) # prints 24
x /= 4 # x = x / 4
print(x) # prints 6.0
x //= 2 # x = x // 2
print(x) # prints 3.0
x **= 3 # x = x ** 3 
print(x) # prints 27.0

#identity operators
# the identity operators include is and is not which are used to compare the memory locations of two objects.
# is = true if both operands refer to the same object in memory
# is not = true if both operands do not refer to the same object in memory 
# is = false if both operands do not refer to the same object in memory
a = [1, 2, 3]
b = a # b refers to the same list as a
c = [1, 2, 3] # c refers to a different list with the same content as a
print(a is b) # prints True because a and b refer to the same object in memory
print(a is c) # prints False because a and c refer to different objects in memory
print(a == c) # prints True because a and c have the same content

#membership operators
#it includes in and not in operators
# in = true if the value is found in the sequence
# not in = true if the value is not found in the sequence
fruits = ["apple", "banana", "cherry"]
print("apple" in fruits) #prints true as apple belongs to the list fruits
print("grape" in fruits) #prints false as grape does not belong to the list fruits
print("grape" not in fruits) #prints true as grape does not belong to the list fruits

#in summary
#arithmetic operators are used to perform mathematical operations on numbers
#comparison operators are used to compare two values and return a boolean value
#logical operators are used to combine multiple conditions and return a boolean value
#assignment operators are used to perform an operation and assign the result to a variable in a single step
#identity operators are used to compare the memory locations of two objects
#membership operators are used to check if a value is present in a sequence (like list, tuple, string etc.)
