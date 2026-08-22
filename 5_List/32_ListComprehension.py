#List Comprehension is a concise way to create lists. 
#It consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses.
#syntax: [expression for item in iterable if condition]

#Example: Create a list of squares of numbers from 0 to 9
sq = [x**2 for x in range(10)]
print(sq) # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#we can also use generator expression to create a list of squares
#syntax: list(expression for item in iterable if condition)
            #expression = x+1 or x**x etc; item = variable = x; iterable= range or list/tuple etc; condition x%2==0;
sqr = list(x**2 for x in range(10))
print(sqr)

#with if condition: Create a list of even numbers from 0 to 9
num = list(x for x in range(10) if x%2 == 0)
print(num) # Output: [0, 2, 4, 6, 8]

#creating list by append method
sqrs = [] #its an empty list
for i in range(1, 11):
    sqrs.append(i**2)
print(sqrs)

#Create a list of Sqrs of Even numbers using append method
EvenSQ = []
for i in range(1, 11):
    if i % 2 == 0:
        EvenSQ.append(i**2)
print(EvenSQ)

#Using List Comprehension

EvenSQ2 = [x**2 for x in range (1, 11) if x % 2 == 0]
print(EvenSQ2)