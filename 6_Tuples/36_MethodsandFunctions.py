#Tuples Methods
#TUples have only 2 methods because they are immutable
colors = "red", "blue", "green", "red", "yellow", "brown", "black", "white", "cyan"
#count   Returns the number of times a specific value appears in the tuple
#syntax: count(element)
print(colors.count("red"))

#index  searches and returns the index of first occurence of the value
#syntax index(element)
print(colors.index("red"))

num = 1,2,3,4,5,6,7,8,9,0
print("Tuple num: ",num)
#But they are compatible with many builtin Functions
#Function               Description
#len(tuple)             Returns the total number of elements in the tuple.
print("Length of tuple: ",len(num))

#max(tuple)             Returns the largest element (elements must be comparable).
print("Max of tuple: ",max(num))

#min(tuple)             Returns the smallest element in the tuple.
print("Min of tuple: ",min(num))

#sum(tuple)             Adds all numeric items together and returns the total.
print("Sum of tuple: ",sum(num))

#sorted(tuple)          Returns a new sorted list containing the tuple's elements.
print("Sorted tuple: ",sorted(num)) #Returns List

#tuple(iterable)        Converts an iterable (like a list or string) into a new tuple.
num2 = tuple(range(1,10))
print(num2)