#Range Function
#the range function is used for generating a sequence of numbers.
#Its commonly used in for loops to specify the number of iterations.
#range() function Syntax:
#range(start, stop, step)

#rang() function accepts 3 parameters:
#start: the starting number of the sequence (inclusive), default is 0
    #inclusive means that the starting number is include in the sequence
#stop: the ending number of the sequence (exclusive), this is required
    #exclusive means that the ending number is not include in the sequence
#step: the increment value between each number in the sequence, DEFAULT is 1

#example of range() function
for i in range(5): #range(stop) - prints 0 to 4
    print(i)

for i in range(1, 6): #range(start,stop) - prints 1 to 5
    print(i)

for i in range(0, 10, 2): #range(start, stop, step) - prints 0, 2, 4, 6, 8
    print(i)

#length = stop - start
#number of iterations = length / step

# we can also use negative step value to generate a sequence in reverse order
for i in range(10, 0, -1): #range(start, stop, step) - prints 10 to 1
    print(i)

# we can also use range() function to generate a sequence of numbers in a list
a = range(5)
print(a) #this prints the range object

# to convert the range object to a list, we can use the list() function
a = list(range(5))
print(a) #this prints the list [0, 1, 2, 3, 4]