import numpy as np
# Filtering in NumPy refers to selecting elements from an array that match a given conditions

ages = np.array([[20, 21, 27, 65, 18, 15, 12, 17],
                 [50, 20, 23, 64, 69, 14, 19, 23]])

teenagers = ages[ages<18] #filtering in NumPy is achieved using masking, here boolean indexing is used to create a mask
# a mask is a boolean array that tells which elements to be included in output array, it has only 0 and 1 values, 0 means False and this value will be excluded while 1 will be included
print(teenagers) # prints all the values less than 18 in a 1D array,
#using boolean indexing, flattens the array to 1D
# we can preserve the shape using wherefunction