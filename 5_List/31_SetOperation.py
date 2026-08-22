#to perform set operations on list 
# we can convert the list to a set and then perform the desired set operations

#Common Elements (Intersection)
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
set1 = set(list1) #converts list1 to a set
set2 = set(list2) #converts list2 to a set

#we find common elements using the intersection() method or the & operator
common_elements = set1.intersection(set2) #finds the common elements between set1 and set2
print(f"Common elements between list1 and list2: {common_elements}") 

#Unique Elements (Union)
#we can find unique elements using the union() method or the | operator
unique_elements = set1.union(set2) #finds the unique elements between set1 and set2
print(f"Unique elements between list1 and list2: {unique_elements}")



#              NESTED LISTS
#A nested list is a list that contains other lists as its elements.

list1 = [1, 2, 3]
list2 = [4, 5, 6]

nested_list = ["Hi", list1, list2, [8, 9, 1000], True, False]
print(nested_list)  # Output: ['Hi', [1, 2, 3], [4, 5, 6], [8, 9, 1000], True, False]