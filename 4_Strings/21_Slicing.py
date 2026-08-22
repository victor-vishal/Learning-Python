#SLICING
#Slicing allows you to access a range of characters in a string using their position (index).
#it starts from 0, from left to right and from -1, from right to left
string = "Hello, World!"
print(string[0:5])  # Output: 'Hello' (characters from index 0 to 4)

#Syntax : string_name[start:stop:step]

#String accepts 3 parameters in slicing, start, stop and step
#start - the index to start slicing from (inclusive)
#stop - the index to stop slicing at (exclusive)
#step - the number of characters to skip between each character in the slice (optional)
print(string[0:5:2])  # Output: 'Hlo' (characters from index 0 to 4, skipping every 2 characters)

#default values for slicing parameters:
#Start - 0 ; Stop - length of the string ; Step - 1
print(string[:5])  # Output: 'Hello' (characters from index 0 to 4)

#negative slicing
#it starts from -1, from right to left
string2 = "Hi My Name is Python"
string3 = string2.strip()  # removing leading and trailing whitespace

#Reversing a string using slicing
print(string3[::-1])  # By passing -1 as step we change the default direction of slicing to reverse the string
#The default values for start is changed from 0 to -1 
# and for stop is changed from length of the string to -len(string)-1
# since we can not define the stop such that it includes 0 indexm we leave it empty and it will automatically include 0 index in the slice
#in short by passing -1 as step we change the direction of slicing... and the default values for start and stop are changed accordingly to include all characters in reverse order.