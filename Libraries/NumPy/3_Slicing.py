import numpy as np

array = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
    ])

# Slicing in NumPy is similar to slicing in Python lists. 
# Syntax: array[start:stop:step]

print(array[::]) #Prints the whole array
print("\n", array[1:3])# prints 2nd and 3rd row

print("\n", array[:4:2]) # prints 1st and 3rd row

print("\n", array[::-1]) # prints the array reversed since direction of traversal is changed



#Column Selection
#Sytax: array[:, column_index]
print("\n", array[:, 1]) # prints 2nd column horizontally

print("\n", array[:, 0:3]) #prints 1st, 2nd and 3rd column vertically
print("\n", array[:, 0:3:2]) #prints 1st and 3rd column vertically

print("\n", array[:, ::-1]) # prints the columns in reverse order

#row and column selection
#syntax: array[rowselect]
print("\n", array[0:2, 0:2]) # prints 1st and 2nd row and 1st and 2nd column (first quadrant)

print(array[0:2, 2:4]) #prints 1st, 2nd row and 3rd, 4th column (second quadrant)
#or
print(array[0:2, 2:]) #prints 1st, 2nd row and 3rd, 4th column (second quadrant)
#if slicing is done till end of array then we can skip the end index