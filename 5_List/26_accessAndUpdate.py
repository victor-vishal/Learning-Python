#Accessing List Elements
lst1 = [10, 20, 30, 40, 50]
print(f"Before updating: {lst1}")
lst1[0] = 100
print(f"After updating: {lst1}")

#Ways to access and update list elements
#1. Using index
lst2 = [1, 2, 3, 4, 5]
print(f"Before updating: {lst2}")
print(lst2[0])  # Output: 1
lst2[0] = 10    
print(f"After updating: {lst2}")  # Output: [10, 2, 3, 4, 5]

#2. Using negative index
print(f"Last element: {lst2[-1]}")  # Output: 5
lst2[-1] = 50
print(f"After updating: {lst2}")  # Output: [10, 2, 3, 4, 50]

#3. Using slicing
print(f"Elements from index 1 to 3: {lst2[1:4]}")  # Output: [2, 3, 4]
lst2[1:4] = [20, 30, 40]
print(f"After updating: {lst2}")  # Output: [10, 20, 30, 40, 50]

#UPDATING MULTIPLE ELEMENTS
lst3 = [1, 2, 3, 4, 5]
print(f"Before updating: {lst3}")
lst3[1:4] = [20, 30, 40]
print(f"After updating: {lst3}")

lst3[1:4] = 3, 4, 5 #we can also update multiple elements without using [] square brackets (tuples are used here i.e if you create a list without using [] square brackets it will be considered as tuple)
print(f"After updating: {lst3}")  
