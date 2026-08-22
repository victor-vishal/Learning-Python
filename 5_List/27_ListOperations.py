#List Operations
#1. Concatenation
#Using + operator we combine two lists to create a new list

lst1 = [1, 2, 3, 4, 5]
lst2 = [6, 7, 8, 9, 10]
lst3 = lst1 + lst2
print(lst3)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#2. Repetition
#* operator is used to repeat the elements of a list a specific number of times
lst4 = [1, 2, 3, "Hello", True]
print(lst4 * 3)  # Output: [1, 2, 3, "Hello", True, 1, 2, 3, "Hello", True, 1, 2, 3, "Hello", True]

#3. Membership
#Checks whether an element belong to a list or not
#Operators used: 
    # in (returns true if elements is presnet)
    # not in (returns true if element is not present)

print(3 in lst4)  # Output: True
print(6 not in lst4)  # Output: True

list5= [1, 2, 3, 4, 5]
print(f"List: {list5}")
inputData = int(input("Enter an element to check: "))

if inputData in list5:
    print(f"{inputData} is present in the list.")
else:    print(f"{inputData} is not present in the list.")

