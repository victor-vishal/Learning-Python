import numpy as np

# Numpy brodcasting is a powerful mechanism that allows Numpy to perform operations on arrays of different shapes.
# It works by virtually expanding dimensions of smaller array to match with the larger array's shape

# for example
# a 4x3 array :           a 1x3 array: ->  this array becomes a 4x3 array by repeating the same row 4 times
# 0 0 0                     1 2 3           1 2 3
# 10 10 10                                  1 2 3
# 20 20 20                                  1 2 3
# 30 30 30                                  1 2 3

# Brodcasting rules:
# 1. If the arrays have the same shape, the operation is performed element-wise.
# 2. If the arrays have different shapes, the smaller array is broadcast to match the larger array's shape.
# 3. The dimensions of the arrays must be compatible for broadcasting to work.
# 4. If the dimensions are not compatible, a VALUE ERROR is raised.

# compatible dimensions are those that are 
# either equal or one of them is 1. 
# For example, (4,3) and (1,3) are compatible, but (4,3) and (2,3) are not.


array1 = np.array([[1,2,3]]) #2d array with a single row
array2 = np.array([[1],[2],[3]]) #2d array with a single column
print(f"array1: \n{array1}, \narray2: \n{array2}")

print("\n",array1.shape)# (1,3)
print(array2.shape)# (3,1)

#since the dimensions are compatible, we can perform element wise addition
result = array1 + array2
print(result)
print(result.shape) # (3,3) since the smaller array is brodcasted to match the larger array's shape

# to avoid confusion
# [[]] the elements in inner bracket are a single row and number or elements in this are the number of columns in that row.
# number of inner brackets means number of rows in the array.

# creatiing a multiplication table using brodcasting

num1 = np.array([[1,2,3,4,5,6,7,8,9,10]]) # 1x10 array
num2 = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])# 10x1 array

print("\nShape of the array1:",num1.shape, "\nShape of the array2:", num2.shape)
print("\nMultiplication:\n", num1 * num2) # 10x10 array