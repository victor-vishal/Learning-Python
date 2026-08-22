#to Find Minimum and Maximum in a List
#we can use the built-in min() and max() functions to find the minimum and maximum values in a list

num = [1,9 , 69, 67, 89 , 21]
print(f"List: {num}")

#syntax: min(iterable) or min(arg1, arg2, *args)
#min() takes an iterable (like a list) or multiple arguments and returns the smallest item among them

min_value = min(num) #finds the minimum value in the list num and assigns it
print(f"Minimum value in the list: {min_value}") #prints the minimum value
print(f"Minimum value among the arguments 6, 7, 1, 4: {min(6, 7, 1, 4)}") #finds the minimum value in the list num and prints it
max_value = max(num) #finds the maximum value in the list num and assigns it
print(f"Maximum value in the list: {max_value}") #prints the maximum value