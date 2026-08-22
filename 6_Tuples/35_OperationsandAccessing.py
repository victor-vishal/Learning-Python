#ACCESS
a = (1,2,3)
print(a)
print(f"a[0] = {a[0]}")
#updating a value in tuple gives error
# a[0] = 2 -> erros

#slicing 
fruits = ("apple", "banana", "cherry", "date", "elderberry")
print(f"{fruits[0:4]}")#prints first 4 element from 0 to 3 index
print("print elements skipping one (fruits[::2]):", fruits[::2])
print("Reversed tuple",fruits[::-1])#elderberry to apple

#OPERATIONS
# Concatenation +
more_fruits = ("melon", "dragonfruit")
print(fruits + more_fruits)

#Repetition *
print("repeating fruits 2 times:", fruits*2)

# Length
print(len(fruits))#prints lenght or number of elements i.e 5

# Membership
print("Is 'apple' in fruits?", "apple" in fruits)
print("Is 'mango' in fruits?", "mango" in fruits)

fruits2= fruits*2
print("Fruits*2= ", fruits2)
