#numPy stands for Numerical Python. It is used in fields that require high-performance mathematical computations, 
# NumPy provides support for large multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays. 
# Since NumPy is written in C, it is much faster than Python's built-in list data structure.

import numpy as np #np is a common alias for NumPy

#print(np.__version__)#2.54

list = [1, 2, 3, 4, 5] #list is a built-in data structure in Python

array = np.array([1, 2, 3, 4, 5]) #array is a NumPy data structure

print(type(list)) #<class 'list'>
print(type(array)) #<class 'numpy.ndarray'>

#numpy arrays also support vectorization
print(array * 2) #[ 2  4  6  8 10] list would duplicate the list instead of multiplying each element by 2