#Tuples just like list is ordered collection of items
#Tuples uses ()
#Tuples are immutable but can have mutable items like list in them
#Tuples are heterogeneous

#Elements are accessed using index a[index]
#we can use indexing, slicing etc a[start: stop(exclusive) : step]

#an empty Tuple
a = ()
print (a) #prints ()

b = (1,2,3,4,5,6)
print(b)
print(b[0]) #prints 1

# b[0] = 9 #Gives an error
# print(b)

lst = ["YO", 1,2]
c = ("hi", 3, 4, lst) #tuples containing mutable items 
print(c)

#Difference Between List and Tuples

# Tuples                                        List
# ()                                            []
# immutable                                     Mutable
# Faster                                        Slower
# Less Memory Usage                             Higher Memory Usage
# Used on constant fixed data                   Used where data changes
