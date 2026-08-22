#List is a mutable data type
#It is a collection of items that are ordered and changeable.
#List can store items of different data types, including numbers, strings, and even other lists.

#Properties of List
#1. ORDERED: The items in a list have defined order
#2. MUTABLE: Items in a list can be changed after the list is created
#3. DYNAMIC: Lists can grow and shrink in size as needed
#4. HETEROGENEOUS: Lists can contain items of different data types

#creation of list
#1. Using square brackets []
my_list = [1, 2, 3, "Hello", 4.5, [5, 6]]
print(my_list)

#2. Using the list() constructor
#it works by taking an iterable (like a string, tuple, or another list) and converting it into a list.
my_list2 = list((1, 2, 3, "Hello", 4.5, [5, 6]))
print(my_list2)

#3. Using list comprehension and range() function
my_list3 = [x for x in range(10)]
print(my_list3)

#List comprehension is a concise way to create lists. It consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses.
#Example: Create a list of squares of numbers from 0 to 9
squares = [x**2 for x in range(10)]
print(squares)