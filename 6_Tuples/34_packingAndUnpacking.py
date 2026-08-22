#Packing and Unpacking
# Packing is the putting multiple values into a single variable (tuple)
fruits = "apple", "banana", "cherry", "date", "elderberry"
print("Packed tuple:", fruits)

#unpacking is the process of assigning the values from a tuple to individual variables
a, b, c, d, e = fruits
print("Unpacked variables:", a, b, c, d, e)
print(a)
#order is important in unpacking, the number of variables on the left must match the number of elements in the tuple on the right

#f, g = fruits#give errors too many values to unpack expected 2, got 5
#This happens because we are trying to unpack 5 values from the tuple into only 2 variables (f and g). 
f, g , *rest = fruits
#to catch remaining values we use * before variable name and it capture the rest value in a list
#the rest contains the remaining values in the tuple after unpacking f and g in a list
print("f=",f,"g=",g, "rest= ",rest)

#to put the middle values in the rest
sports = "Swimming", "SKating", "Surfing", "GLiding"
print(sports)

first, *middle, last = sports
print(f"First: {first}, Middle: {middle}, last: {sports}")
#Using * is called extended unpacking and it stores the element in a list







# Unpacking
# print("\nUnpacking:")
# a, b, c, d, e = fruits
# print("Unpacked:", a, b, c, d, e)

# # Partial unpacking with *
# first, *middle, last = fruits
# print("Partial unpacking (first, *middle, last):", first, middle, last)

# Note: Tuples are immutable, so you cannot modify them directly
# fruits[0] = "apricot"  # This would raise an error

# print("\nTuples are immutable - you can't change elements after creation!")


# Methods & FunctionsBecause they are immutable, tuples have very few built-in methods:
# Methods.count(x): Returns the number of times x appears..
# index(x): Returns the first index where x is found.
# Built-in Functionslen(): Get the total length.type(): Confirms it is <class 'tuple'>.
# max() / min(): Find the highest or lowest value.
# sum(): Add up all numerical elements.
# 
# 
# 5. Pro-Tips & Hidden FeaturesThe "Workaround": To change a tuple, convert it to a list (list(tpl)), modify it, then convert it back (tuple(lst)).Named Tuples: Part of the collections module; they allow you to access elements by name instead of just index.Memory Efficiency: Use tuples for large datasets that won't change to save RAM.