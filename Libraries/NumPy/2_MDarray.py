import numpy as np

# 0 Dimensional Array 
array = np.array("A")# a single point

#to print dimension of array we used ndim attribute
print(array.ndim)

# 1D array
array = np.array((1,2,3,4))
print(array.ndim)

# 2d arraya
array = np.array([list(range(5)), list(range(5))])
print (array)
print(array.ndim)

# array = np.array([[list(range(4)), list(range(4)), list range(4)]]) #[ [], [], []  ]
array = np.array([[list(range(4)), list(range(4)), list(range(4))]])
print(array)
print(array.ndim)

# to create more dimension we increae [] basically nested list
# for eg to create a nd array we can use n nested list
#1d array = ["A", "B", "C"]
#2d array = [["A", "B", "C"], ["D", "E", "F"]]
ThreeDArray = np.array(
    [
    [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]],
    [["J", "K", "L"], ["M", "N", "O"], ["P", "Q", "R"]],
    [["S", "T", "U"], ["V", "W", "X"], ["Y", "Z","__PlaceHolder__"]] # nummber of elements in each nested list should be same otherwise it will give error because of inhomogeneous shape
    ]
)
print(ThreeDArray)
print(f"Dimension of above array is {ThreeDArray.ndim}")
print(f"Shape of above array is {ThreeDArray.shape}")

array = np.array([[[[[1,2,3,4]]]]]) #5 D array
print(array.ndim)
print(array.shape)

#Shape, shape attribute returns a tuple of ints indicating the size of the array in each dimension.
# where first element is the size of first dimension and so on!

#ACCESSING ELEMENTS!

# Chain Indexing: Just like lists
print(ThreeDArray[0][0][0]) #A

#NumPy uses Multi-dimensional indexing: You can access elements in a multi-dimensional array using a single set of square brackets and a comma-separated list of indices.
print(ThreeDArray[0, 0, 0]) #A
print(ThreeDArray[0,0, 1]) #B
# print(ThreeDArray[0, 0, 3]) #IndexError: index 3 is out of bounds for axis 2 with size 3

# MULTIDIMENSIONAL INDEXING IS FASTER THAN CHAIN INDEXING

#Forming a word using string concatenation from ThreeDArray

word = ThreeDArray[2, 1, 0] + ThreeDArray[0, 2, 2] + ThreeDArray[1, 0, 1] + ThreeDArray[2, 0, 1] + ThreeDArray[1, 1, 2] + ThreeDArray[1, 2, 2]

print(word) # Prints VIKTOR