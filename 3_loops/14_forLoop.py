#for loop in python is used to iterate over a sequence (like a list, tuple, dictionary, set, or string) or other iterable objects.
# syntax:
# for variable in sequence:
    # code to be executed

# example of for loop
a = [1, 2, 3, 4, 5]
for i in a:
    print(i)
# we can also use for loop to iterate over a string
s = "Hello"
for i in s:
    print(i)

#if we dont want to iterate over a sequence but want to execute a block of code a specific number of times, we can use the range() function in for loop

for i in range(5):
    print(i) #prints 0 to 4

for i in range(1, 6):
    print(i) #prints 1 to 5

for i in range(0, 10, 2):
    print(i) #prints 0, 2, 4, 6, 8


#PRINTING ITERABLES SIDE BY SIDE
# to print the iterables side by side we can use the end parameter of the print() function
for i in range(5):
    print(i, end=' ') #prints 0 1 2 3 4
#the end parameter of print() specifies the string that is printed at the end fo output
#by default, then end parameter is set to\n
#thus the cursor is move to new line after each print statement