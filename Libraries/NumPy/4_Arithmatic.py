import numpy as np

# Scaler arithmatic operations
array = np.array([1,2,3,4])
# a scalar is a single value, when we perform operation with a scalar and an array, it is applied to each element of the array.
print(array + 2) # adds 2 to each element of the array
print(array - 2) # subtracts 2 from each element of the array
print(array * 3) # multiplies each element of the array by 3
print(array / 2) # divides each element of the array by 2
print(array ** 5) # raises each element of the array to the power of 5

#VECTORIZED MATH OPERATIONS
# A vector is a one dimensional array
# vectorized operations allow us to perform mathematical operations on entire vectors (or arrays) without the need for explicit loops.
array = np.array([1.2, 2.5, 3.7, 4.1])
print(np.sqrt(array)) # returns the square root of each element in the array
print(np.exp(array)) # returns the exponential of each element in the array
print(np.round(array)) # rounds each element in the array to the nearest integer
#to round down we use floor and to round up we use ceil
print(np.floor(array)) # rounds down each element in the array to the nearest integer
print(np.ceil(array)) # rounds up each element in the array to the nearest integer

# numpy has built in constants as well, for example pi and e
print(f"{np.pi:.2f}") # returns the value of pi

#print area of circle with radius 5
r = np.array((2,1,3,4))
print(np.pi * r ** 2)



# Element wise arithmetic operations
array1 = np.array([1,2,3,4])
array2 = np.array([5,6,7,8])

print (array1 + array2) 
print (array1 - array2)
# similarly we can perform *, /, ** operations as well
# to concatenate two arrays we can use np.concatenate() function
array3 = np.concatenate((array1, array2))
print(array3) # prints [1 2 3 4 5 6 7 8]



# Comparison operators
score = np.array([90, 80, 30, 60])
print(score > 50) # returns a boolean array of True and False values based on the comparison

score[score < 50] = 0 # replace values < 50 to 0
#it is called boolean indexing or masking
# Syntax: array[mask] = value 
# mask is a boolean array of the same shape as the original array, where True indicates the elements to be replaced and False indicates the elements to be kept unchanged.
# score[True] = 0 replace all values to 0 since True is passed instead of mask
print(score) # prints [90 80  0 60] since the value less than 50 is replaced with 0