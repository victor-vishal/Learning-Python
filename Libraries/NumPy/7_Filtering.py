import numpy as np
# Filtering in NumPy refers to selecting elements from an array that match a given conditions

ages = np.array([[20, 21, 27, 65, 18, 15, 12, 17],
                 [50, 20, 23, 64, 69, 14, 19, 23]])

teenagers = ages[ages<18] #filtering in NumPy is achieved using masking, here boolean indexing is used to create a mask
# a mask is a boolean array that tells which elements to be included in output array, it has only 0 and 1 values, 0 means False and this value will be excluded while 1 will be included
print(teenagers) # prints all the values less than 18 in a 1D array,


adults = ages[(ages>=18) & (ages<65)] #we use & instead of and, because numpy uses C style logical operators,
print(adults)

senior = ages[ages>=65]
print(senior)

evenAge = ages[ages%2 == 0]
oddAge = ages[ages % 2 != 0]
print("Even Ages: ", evenAge)
print("Odd Ages: ", oddAge)

# using boolean indexing, flattens the array to 1D
# we can preserve the shape using wherefunction
# Synatx: np.where(condtion, container, alternative or fill value))
adults = np.where(ages>=18, ages, 0) # 0 as fill values means all the elements that dont satisfy the conditions will be replaced by 0
print(adults)
#[[20 21 27 65 18  0  0  0] 15, 12, 17 replaced with 0 as they are <18
# [50 20 23 64 69  0 19 23]]

# using np.where() keeps the shape of array, but it is slower than boolean indexing