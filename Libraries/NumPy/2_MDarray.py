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
    [["S", "T", "U"], ["V", "W", "X"], ["Y", "Z","__PlaceHolder__"]]
    ]
)
print(ThreeDArray)