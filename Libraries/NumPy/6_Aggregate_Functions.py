import numpy as np

# Aggregate functions in NumPy are used to perfrom operations on entire arrays and return a single value as output. 
# These functions are useful for summarizing data and extracting meaningful information from large datasets.
# Functions are:
# 1. np.sum() - returns the sum of all elements in the array
# 2. np.prod() - returns the product of all elements in the array
# 3. np.mean() - returns the mean of all elements in the array
# 4. np.median() - returns the median of all elements in the array
# 5. np.std() - returns the standard deviation of all elements in the array
# 6. np.var() - returns the variance of all elements in the array

np.array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print ("Sum of all elements in the array:" ,np.sum(np.array)) # returns the sum of all elements in the array
print("Product of all elements in the array:", np.prod(np.array))
print(f"Minimum value: {np.min(np.array)} at position: {np.argmin(np.array)}") # returns the min value and its position
print(f"Maximum value: {np.max(np.array)} at position: {np.argmax(np.array)}") # returns the max value and its position
print(f"Mean: {np.mean(np.array)}")
print(f"Median: {np.median(np.array)}")
print(f"Standard Deviation: {np.std(np.array)}")
print(f"Variance: {np.var(np.array):.3f}")

# Check if std square equals variance
stdsq = (np.std(np.array) ** 2)
variance = np.var(np.array)
# stdsqstr = f"{stdsq:.2f}"
# varstr = f"{variance:.2f}"
print(f"{stdsq:.2f}" == f"{variance:.2f}")

#another way is to use np.isclose() function,  it checks if 2 values are close enough to be considered equal, (with a small tolerance of about 10^-8) 
# It is very useful when comparing floats, it also avoid string conversion overhead
print(np.isclose(stdsq, variance)) # returns True or False,
# Synatx :np.isclose(a,b) or  np.isclose(a, b, rtol=1e-05, atol=1e-08, equal_nan=False) 
# where rtol is relative tolerance, atol is absolute tolerance, equal_nan is a boolean that indicates whether to consider NaNs as equal or not.

# to sum all columns or rows of a 2D array, we can use the axis parameter in the np.sum() function.
print("sum of all columns:", np.sum(np.array, axis=0)) #axis 0 for columns, axis 1 for rows
print("sum of all rows:", np.sum(np.array, axis=1))